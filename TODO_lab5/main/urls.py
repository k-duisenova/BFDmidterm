from django.urls import path

from main.views import TodoListAPIView, TodoListIdAPIView, TodoAPIView

urlpatterns = [
    path('todos', TodoListAPIView.as_view()),
    path('todos/<int:pk>', TodoListIdAPIView.as_view()),
    path('todos/<int:id>/completed', TodoAPIView.as_view()),
]
