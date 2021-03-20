from rest_framework import serializers
from .models import Book, BookJournalBase, Journal


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    num_pages = serializers.IntegerField()
    genre = serializers.CharField(max_length=50)

    def create(self, validated_data):
        book = Book.objects.create(name=validated_data.get('name'), price=validated_data.get('price'),
                                   description=validated_data.get('description'), created_at=validated_data.get('created_at'),
                                   num_pages=validated_data.get('num_pages'), genre=validated_data.get('genre'))
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.num_pages = validated_data.get('num_pages', instance.num_pages)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance


class JournalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    type = serializers.CharField()
    publisher = serializers.CharField(max_length=255)

    def create(self, validated_data):
        journal = Journal.objects.create(name=validated_data.get('name'), price=validated_data.get('price'),
                                            description=validated_data.get('description'), created_at=validated_data.get('created_at'),
                                            type=validated_data.get('type'), publisher=validated_data.get('publisher'))
        return journal

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.type = validated_data.get('type', instance.type)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.save()
        return instance