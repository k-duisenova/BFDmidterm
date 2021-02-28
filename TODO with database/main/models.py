from django.db import models


class TodoList(models.Model):
    id = models.IntegerField(primary_key=True)


class Todo(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    due_on_date = models.DateTimeField()
    owner = models.CharField(max_length=100)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    category = models.CharField(max_length=40, default='Incomplete')

    def __str__(self):
        return self.name
