import pytest

from rest_framework import status
from rest_framework.test import APIClient


class TestNewsArticleAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_get_news_articles_api_view_status_200(self, api_client):
        response = api_client.get("/api/v1/articles")
        assert response.status_code == status.HTTP_200_OK

    def test_get_news_articles_api_view_status_404(self, api_client):
        response = api_client.get("/api/v1/invalid-url")
        assert response.status_code == status.HTTP_404_NOT_FOUND
