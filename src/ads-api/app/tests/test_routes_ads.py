import pytest

from fastapi.testclient import TestClient

from app.app import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_read_ads_get_view_block_renderer_js(client):
    response = client.get("/ads.getViewBlock?renderer=js")
    assert response.status_code == 200

    json = response.json()
    assert "success" in json
    assert "v" in json


def test_read_ads_get_view_block_renderer_html(client):
    response = client.get("/ads.getViewBlock?renderer=html")
    assert response.status_code == 200