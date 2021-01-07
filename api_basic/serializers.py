from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()


    def create(self, validated_data):
        return Article.objects.create(validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.article = validated_data.get('article', instance.article)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
