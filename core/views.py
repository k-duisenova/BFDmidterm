from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from core.models import Book, Journal
from core.serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser, )

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        book_data = request.data
        new_book = Book.objects.create(name=book_data['name'], price=book_data['price'],
                                       created_at=book_data['created_at'], description=book_data['description'],
                                       genre=book_data['genre'], num_pages=book_data['num_pages'])
        new_book.save()
        serializer = BookSerializer(new_book)
        return Response(serializer.data)

    def destroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request):
        print(request.data['result'])


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser,)

    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        journal_data = request.data
        new_journal = Journal.objects.create(name=journal_data['name'], price=journal_data['price'],
                                       created_at=journal_data['created_at'], description=journal_data['description'],
                                       genre=journal_data['genre'], num_pages=journal_data['num_pages'])
        new_journal.save()
        serializer = BookSerializer(new_journal)
        return Response(serializer.data)

    def destroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request):
        print(request.data['result'])
