from flask import render_template, request, Blueprint
from flask_login import login_required

from flaskblog.models import Product
from sqlalchemy import case

main = Blueprint('main', __name__)



@main.route("/products")
@login_required
def products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.name.asc()).paginate(page=page, per_page=5)
    return render_template('products.html', title='Products', products=products)


@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')

# @main.route("/products")
# def products():
#     page = request.args.get('page', 1, type=int)
#     posts = Product.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
#     return render_template('products.html', title='Products', posts=posts)

