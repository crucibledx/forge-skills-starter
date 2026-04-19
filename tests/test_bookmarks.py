from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_bookmark():
    response = client.post(
        "/bookmarks",
        json={"url": "https://example.com", "title": "Example", "tags": ["test"]},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Example"
    assert len(data["tags"]) == 1

    bookmark_id = data["id"]
    response = client.get(f"/bookmarks/{bookmark_id}")
    assert response.status_code == 200


def test_list_bookmarks():
    response = client.get("/bookmarks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
