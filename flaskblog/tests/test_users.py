def test_register(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword'
    }, follow_redirects=True)

    assert response.status_code == 200


def test_login_logout(client):
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword'
    })

    # Login
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)
    assert response.status_code == 200

    # Logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

