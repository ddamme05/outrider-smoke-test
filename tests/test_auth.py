def test_register_and_login(client):
    payload = {"email": "ada@example.com", "display_name": "Ada", "password": "correct horse"}
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 201
    assert response.json()["email"] == "ada@example.com"

    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    assert response.json()["access_token"]
