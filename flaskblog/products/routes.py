from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, session)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.logs.logging import log_to_couchdb
from flaskblog.models import Product
from flaskblog.products.forms import ProductForm

products = Blueprint('products', __name__)


@products.route("/product/new", methods=['GET', 'POST'])
@login_required
def new_product():
    if not current_user.has_roles('admin'):
        abort(403)
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(\
            name=form.name.data,\
            category=form.category.data,\
            price=form.price.data,\
            quantityInStock=form.quantityInStock.data,\
            unitOfMeasure=form.unitOfMeasure.data,\
            description=form.description.data)
        db.session.add(product)
        db.session.commit()
        log_to_couchdb(f"User with id:{current_user.id} created product:{product.id} {product.name}!")
        flash('Your product has been created!', 'success')
        return redirect(url_for('main.products'))
    return render_template('create_product.html', title='New Product',
                           form=form, legend='New Product')


@products.route("/products/<string:category>")
@login_required
def category_products(category):
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter_by(category=category).order_by(Product.name.asc()).paginate(page=page, per_page=5)
    if not products.items: 
        abort(404)

    return render_template('category_products.html', products=products, category=category)


@products.route("/product/<int:product_id>")
@login_required
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)


@products.route("/product/<int:product_id>/update", methods=['GET', 'POST'])
@login_required
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if not current_user.has_roles('admin'):
        abort(403)
    form = ProductForm()
    if form.validate_on_submit():
        product.name=form.name.data
        product.category=form.category.data
        product.price=form.price.data
        product.quantityInStock=form.quantityInStock.data
        product.unitOfMeasure=form.unitOfMeasure.data
        product.description=form.description.data

        db.session.commit()
        log_to_couchdb(f"User with id:{current_user.id} updated product:{product.id} {product.name}!")
        flash('Your product has been updated!', 'success')
        return redirect(url_for('products.product', product_id=product.id))
    elif request.method == 'GET':
        form.name.data = product.name
        form.category.data = product.category
        form.price.data = product.price
        form.quantityInStock.data = product.quantityInStock
        form.unitOfMeasure.data = product.unitOfMeasure
        form.description.data = product.description

    return render_template('create_product.html', title='Update Product',
                           form=form, legend='Update Product')


@products.route("/product/<int:product_id>/delete", methods=['POST'])
@login_required
def delete_product(product_id):
    if not current_user.has_roles('admin'):
        abort(403)
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    log_to_couchdb(f"User with id:{current_user.id} deleted product:{product.id} {product.name}!")
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.products'))

@login_required
@products.route('/add_to_cart/<string:product_id>')
def add_to_cart(product_id):
    page = request.args.get('page', 1, type=int)
    quantityInStock = request.args.get('quantityInStock', 0, type=int)

    session.get('cart', {})
  
    cart = session['cart']

    if product_id in cart:
        if quantityInStock < session['cart'][product_id]:
            flash('You chose more items than in stock. Please choose another quantity', 'danger')
            return redirect(url_for('main.products', page=page))
        else:
            cart[product_id] += 1
    else:
        cart[product_id] = 1

    session['cart'] = cart
    print(cart)
    return redirect(url_for('main.products', page=page))

@login_required
@products.route('/cart')
def cart():
    page = request.args.get('page', 1, type=int)
    cart = session.get('cart', {})
    products = Product.query.filter(Product.id.in_(list(cart.keys())))    # get products list from database which were added to cart 
    total_price = calculate_total_price(cart, products)
    products = products.paginate(page=page, per_page=5)
    return render_template('cart.html', products=products, cart=cart, total_price=total_price)

def calculate_total_price(cart, products):
    total_price = 0.0
    for product in products:
        quantity = cart[str(product.id)]
        total_price += product.price * quantity
    return total_price

@login_required
@products.route('/cart/<int:product_id>/update')
def update_cart_item(product_id):
    page = request.args.get('page', 1, type=int)
    quantityInStock = request.args.get('quantityInStock', 0, type=int)
    new_quantity = request.args.get('new_quantity', 1, type=int)
    cart = session.get('cart', {})

    if quantityInStock < new_quantity:
        flash('You chose more items than in stock. Please choose another quantity', 'danger')
        return redirect(url_for('/cart', page=page))
    
    if new_quantity < 0:
        flash('Wrong quantity. Please choose another quantity', 'danger')
        return redirect(url_for('/cart', page=page))

    cart[product_id] = new_quantity

    session['cart'] = cart

    return redirect(url_for('/cart', page=page))
