from django.urls import path

from .views import NewsArticlesAPIView

urlpatterns = [
    path("articles", NewsArticlesAPIView.as_view(), name="news-articles-api"),
]
