import pytest
from flaskblog import create_app, db
from flaskblog.models import User, Product
from flaskblog.products.forms import ProductForm


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def test_new_product_route(client, app):
    # Assuming you have a user with admin role in your test database
    login(client, 'admin_user', 'admin_password')

    response = client.get('/product/new')
    assert response.status_code == 302

    response = client.post('/product/new', data=dict(
        name='Test Product',
        category='Test Category',
        price=10.0,
        quantityInStock=5,
        unitOfMeasure='Test UOM',
        description='Test Description'
    ), follow_redirects=True)

    assert response.status_code == 200


def test_category_products_route(client):
    response = client.get('/products/Test_Category')
    assert response.status_code == 302


def test_product_route(client):
    product = Product(name='Test Product', category='Test Category', price=10.0, quantityInStock=5,
                      unitOfMeasure='Test UOM', description='Test Description')
    db.session.add(product)
    db.session.commit()

    response = client.get(f'/product/{product.id}')
    assert response.status_code == 302


def test_update_product_route(client, app):
    # Assuming you have a user with admin role in your test database
    login(client, 'admin_user', 'admin_password')

    product = Product(name='Test Product', category='Test Category', price=10.0, quantityInStock=5,
                      unitOfMeasure='Test UOM', description='Test Description')

    db.session.add(product)
    db.session.commit()

    response = client.get(f'/product/{product.id}/update')
    assert response.status_code == 302

    response = client.post(f'/product/{product.id}/update', data=dict(
        name='Updated Test Product',
        category='Updated Test Category',
        price=15.0,
        quantityInStock=10,
        unitOfMeasure='Updated Test UOM',
        description='Updated Test Description'
    ), follow_redirects=True)

    assert response.status_code == 200


def test_delete_product_route(client, app):
    # Assuming you have a user with admin role in your test database
    login(client, 'admin_user', 'admin_password')

    product = Product(name='Test Product', category='Test Category', price=10.0, quantityInStock=5,
                      unitOfMeasure='Test UOM', description='Test Description')
    db.session.add(product)
    db.session.commit()

    response = client.post(f'/product/{product.id}/delete', follow_redirects=True)
    assert response.status_code == 200
