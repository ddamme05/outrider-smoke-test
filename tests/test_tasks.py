def _token(client) -> str:
    payload = {"email": "grace@example.com", "display_name": "Grace", "password": "compiler"}
    client.post("/auth/register", json=payload)
    return client.post("/auth/login", json=payload).json()["access_token"]


def test_create_and_list_tasks(client):
    token = _token(client)
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/tasks",
        headers=headers,
        json={"title": "Review queue", "description": "Check risky diffs", "tag_names": ["review"]},
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Review queue"

    response = client.get("/tasks", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
