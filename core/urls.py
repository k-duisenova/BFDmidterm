from django.urls import path

from core.views import BookViewSet, JournalViewSet

urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('journals/', JournalViewSet.as_view({'get': 'list'}))
]