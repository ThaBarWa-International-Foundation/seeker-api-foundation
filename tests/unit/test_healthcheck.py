def test_hello_world(client):
    # Send a GET request to the healthcheck URL
    response = client.get('/ping')

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.data == b'pong'
