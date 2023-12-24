from flask import render_template, request, Blueprint, session
from flask_login import login_required, current_user

from flaskblog.models import Product, Orders
import json

main = Blueprint('main', __name__)



@main.route("/products")
@login_required
def products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.name.asc()).paginate(page=page, per_page=5)
    return render_template('products.html', title='Products', products=products)

@login_required
@main.route('/cart')
def cart():
    page = request.args.get('page', 1, type=int)
    cart = session.get('cart', {})
    cart = dict(sorted(cart.items()))
    products = Product.query.filter(Product.id.in_(list(cart.keys())))    # get products list from database which were added to cart 
    total_price = round(calculate_total_price(cart, products),2)
    products = products.paginate(page=page, per_page=5)
    return render_template('cart.html', products=products, cart=cart, total_price=total_price)

def calculate_total_price(cart, products):
    total_price = 0.0
    for product in products:
        quantity = cart[str(product.id)]
        total_price += product.price * quantity
    return total_price

@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')

@main.route("/orders")
@login_required
def orders():
    page = request.args.get('page', 1, type=int)
    
    orders = Orders.query.filter(Orders.userId == current_user.id).order_by(Orders.orderDate.desc())
    print(orders)
    
    products_list=[]
    cart_dict={}
    for order in orders:
        cart_dict = json.loads(order.orderedProducts)
        cart_dict = dict(sorted(cart_dict.items()))

        products = Product.query.filter(Product.id.in_(list(cart_dict.keys())))
        products_list.append(products)
    
    orders = orders.paginate(page=page, per_page=5)
    return render_template('orders.html', title='Orders', orders=orders, products_list=products_list, cart_dict=cart_dict, zip=zip)

