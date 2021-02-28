from django.shortcuts import render
from datetime import datetime, timedelta

todos = [
        {
            'name': 'Finish the book',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=6),
            'owner': 'Kuralay',
            'mark': False
        },
        {
            'name': 'Buy the present',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=1),
            'owner': 'Kuralay',
            'mark': False
        },
        {
            'name': 'Send the EA assignment',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=3),
            'owner': 'Kuralay',
            'mark': True
        },
        {
            'name': 'Bake a banana bread',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=2),
            'owner': 'Kuralay',
            'mark': False
        },
        {
            'name': 'Try dance workouts',
            'created_date': datetime.now(),
            'due_on_date': datetime.now() + timedelta(days=1),
            'owner': 'Kuralay',
            'mark': True
        }

    ]


def todos_list(request):

    context = {
        'todos': todos
    }

    return render(request, 'todos_list.html', context=context)


def completed_todos_list(request):

    context = {
        'todos': todos
    }
    return render(request, 'completed_todos_list.html', context=context)
