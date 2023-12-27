from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, session)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.logs.logging import log_to_couchdb
from flaskblog.models import Orders, Product
from flaskblog.products.forms import ProductForm
import json

orders = Blueprint('orders', __name__)


@login_required
@orders.route('/add_order')
def add_order():
    page = request.args.get('page', 1, type=int)
    cart = session.get('cart')
    products = Product.query.filter(Product.id.in_(list(cart.keys())))
    total_price = calculate_total_price_and_update_db(cart, products)

    if total_price == -1:
        return redirect(url_for('main.cart', page=page))

    if (total_price < 0.009):
        flash('Cant order, wrong total price', 'danger')
        return redirect(url_for('main.cart', page=page))

    cart_json = json.dumps(cart)
    new_order = Orders(
        userId=current_user.id,
        orderedProducts=cart_json,
        totalAmount=total_price,
        orderStatus='Pending',  # Default status before manager changes it
        warehouseId=1
        # TODO: check available products on warehouses closest to user location, and create multiple orders for each warehouse respectively to available products
    )
    db.session.add(new_order)
    db.session.commit()
    log_to_couchdb(
        f"User with id:{current_user.id} created order:{new_order.id} with items {new_order.orderedProducts} with total price {new_order.totalAmount}!")
    flash('Your order has been created!', 'success')

    session['cart'] = {}  # clear session cart
    return redirect(url_for('main.orders'))  # redirect to user orders page


def calculate_total_price_and_update_db(cart, products):
    total_price = 0.0
    is_enough_products = True
    for product in products:
        quantity = cart[str(product.id)]
        total_price += product.price * quantity
        new_quantity = product.quantityInStock - quantity
        product.quantityInStock -= quantity
        db.session.add(product)  # add change to db

        if (new_quantity < 0):
            is_enough_products = False
            flash(
                f"Sorry, seems like we dont have enough amount of \'{product.name}\' to sutisfy your order. Please change your cart",
                'danger')

    db.session.flush()  # save changes (but not write) to db

    if is_enough_products:
        db.session.commit()  # write changes to db
        return total_price
    else:
        db.session.rollback()  # discard changes
        return -1
