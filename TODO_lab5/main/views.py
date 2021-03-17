from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoListModelSerializer, TodoModelSerializer, TodoSerializer, TodoListSerializer
from .models import Todo, TodoList
from django.contrib import auth

# def login(request):
#     username = request.POST('username')
#     password = request.POST('password')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect("/todos")
#     else:
#         return HttpResponseRedirect("/")


class TodoListAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoModelSerializer(todos, many=True)
        return render(request, "todos_list.html", {"todos": serializer.data})


class TodoListIdAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return TodoList.objects.get(name=pk)
        except TodoList.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, pk):
        todo_list = self.get_object(pk)
        todos = Todo.objects.filter(list_id=pk)
        serializer = TodoModelSerializer(todos, many=True)
        return render(request, "todos_list.html", {"todos": serializer.data, "todo_list": todo_list})


class TodoAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, id):
        try:
            return TodoList.objects.get(name=id)
        except TodoList.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        todo_list = self.get_object(id)
        completed_todos = Todo.objects.filter(list_id=id, category='Completed')
        serializer = TodoModelSerializer(completed_todos, many=True)
        return render(request, "completed_todos_list.html", {"todos": serializer.data, "todo_list": todo_list})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def all_todos(request):
    todos = Todo.objects.all()
    return render(request, "todos_list.html", {"todos": todos})


def todos_list(request, pk):
    todos = Todo.objects.filter(category='Incomplete', list_id=pk)
    todo_list = TodoList.objects.get(id=pk)
    return render(request, "todos_list.html", {"todos": todos, "todo_list": todo_list})


def completed_todos_list(request, id):
    completed_todos = Todo.objects.filter(list_id=id, category='Completed')
    todo_list = TodoList.objects.get(id=id)
    return render(request, "completed_todos_list.html", {"todos": completed_todos, "todo_list": todo_list})
