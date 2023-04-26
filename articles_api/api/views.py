from django.conf import settings
from newsapi import NewsApiClient
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewsArticlesSerializers


class NewsArticlesAPIView(APIView):
    def get(self, request):
        newsapi_client = NewsApiClient(api_key=settings.NEWS_API_KEY)
        results = newsapi_client.get_top_headlines()
        articles = []
        for article_data in results["articles"]:
            article = {
                "author": article_data["author"],
                "title": article_data["title"],
                "description": article_data["description"],
            }
            articles.append(article)
        serializer = NewsArticlesSerializers(articles, many=True)
        return Response(serializer.data)
