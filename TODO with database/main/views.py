from django.shortcuts import render
from .models import Todo, TodoList


def todos_list(request):
    todos = Todo.objects.filter(category='Incomplete')
    return render(request, "todos_list.html", {"todos": todos})


def completed_todos_list(request):
    completed_todos = Todo.objects.filter(category='Completed')
    return render(request, "completed_todos_list.html", {"todos": completed_todos})
