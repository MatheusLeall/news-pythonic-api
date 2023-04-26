from rest_framework import serializers


class NewsArticlesSerializers(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
