from flaskblog import db
from flaskblog.models import User, Notification, Orders
from flaskblog.tests.test_products import login


def test_products_route(client, app):
    with app.app_context():
        response = client.get('/products')
        assert response.status_code == 302

        admin_user = User(username='admin_user', email='admin@example.com', password='admin_password')
        db.session.add(admin_user)
        db.session.commit()

        login(client, 'admin_user', 'admin_password')
        response = client.get('/products')
        assert response.status_code == 302


def test_cart_route(client, app):
    with app.app_context():
        response = client.get('/cart')
        assert response.status_code == 200

        test_user = User(username='test_user', email='test@example.com', password='test_password')
        db.session.add(test_user)
        db.session.commit()

        with client.session_transaction() as sess:
            sess['cart'] = {'1': 2, '3': 1}

        login(client, 'test_user', 'test_password')
        response = client.get('/cart')
        assert response.status_code == 200

def test_orders_route(client, app):
    with app.app_context():
        response = client.get('/orders')
        assert response.status_code == 302

        test_user = User(username='test_user', email='test@example.com', password='test_password')
        db.session.add(test_user)
        db.session.commit()

        login(client, 'test_user', 'test_password')
        response = client.get('/orders')
        assert response.status_code == 302


def test_all_orders_route(client, app):
    with app.app_context():
        response = client.get('/all_orders')
        assert response.status_code == 302

        admin_user = User(username='admin_user', email='admin@example.com', password='admin_password')
        db.session.add(admin_user)
        db.session.commit()

        login(client, 'admin_user', 'admin_password')
        response = client.get('/all_orders')
        assert response.status_code == 302


def test_change_order_status_route(client, app):
    with app.app_context():
        admin_user = User(username='admin_user', email='admin@example.com', password='admin_password')
        db.session.add(admin_user)
        db.session.commit()

        login(client, 'admin_user', 'admin_password')

        order = Orders(userId=admin_user.id, orderedProducts='{"1": 2}', orderStatus='Pending')
        db.session.add(order)
        db.session.commit()

        response = client.get(f'/change_order_status/{order.id}')
        assert response.status_code == 302


def test_delete_notification_route(client, app):
    with app.app_context():
        test_user = User(username='test_user', email='test@example.com', password='test_password')
        db.session.add(test_user)
        db.session.commit()

        login(client, 'test_user', 'test_password')

        notification = Notification(message='Test Notification', userId=test_user.id)
        db.session.add(notification)
        db.session.commit()

        response = client.post(f'/delete_notification/{notification.id}')
        assert response.status_code == 302
