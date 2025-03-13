import pytest
import requests

BASE_URL = "https://yougile.com/api-v2/projects"
HEADERS = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}


def test_create_project():
    payload = {
        "title": (
            "You can't transmit the sensor without programming "
            "the redundant TCP circuit!"
        )
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_update_project():
    project_id = "6f550ed7-22fc-45f5-b8ae-b8d3e4f80618"
    payload = {
        "title": "Updated Project Title"
    }
    response = requests.put(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS,
        json=payload
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


def test_get_project():
    project_id = "6f550ed7-22fc-45f5-b8ae-b8d3e4f80618"
    response = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert "title" in data
    assert "timestamp" in data


@pytest.mark.parametrize("project_id, expected_status", [
    ("invalid_id", 404),
    ("6f550ed7-22fc-45f5-b8ae-b8d3e4f80618", 200)
])
def test_get_project_with_params(project_id, expected_status):
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == expected_status


@pytest.mark.parametrize("payload, expected_status", [
    ({"title": ""}, 400),
    ({"title": "Another Test Project"}, 201)
])
def test_create_project_with_params(payload, expected_status):
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == expected_status
