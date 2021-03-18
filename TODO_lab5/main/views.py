from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoListModelSerializer, TodoModelSerializer, TodoSerializer, TodoListSerializer
from .models import Todo, TodoList

# def login(request):
#     username = request.POST('username')
#     password = request.POST('password')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect("/todos")
#     else:
#         return HttpResponseRedirect("/")


class TodoListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = TodoList.objects.all()
        serializer = TodoListModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TodoList.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TodoListSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        todoList_data = request.data
        new_todoList = TodoList.objects.create(name=todoList_data['name'])
        new_todoList.save()
        serializer = TodoListModelSerializer(new_todoList)
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


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()


class CompletedTodoViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Todo.objects.filter(category='Completed')
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todos = Todo.objects.filter(category='Completed', list_id=pk)
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)

    def create(self, request):
        todo_data = request.data
        new_todo = Todo.objects.create(name=todo_data['name'], created_date=todo_data['created_date'],
                                       due_on_date=todo_data['due_on_date'], owner=todo_data['owner'],
                                       category=todo_data['category'], list_id=todo_data['list_id'])
        new_todo.save()
        serializer = TodoModelSerializer(new_todo)
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

# API Views

# class TodoListAPIView(APIView):
#     permission_classes = (IsAuthenticated, )
#
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoModelSerializer(todos, many=True)
#         return render(request, "todos_list.html", {"todos": serializer.data})
#
#
# class TodoListIdAPIView(APIView):
#     permission_classes = (IsAuthenticated, )
#
#     def get_object(self, pk):
#         try:
#             return TodoList.objects.get(name=pk)
#         except TodoList.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def get(self, request, pk):
#         todo_list = self.get_object(pk)
#         todos = Todo.objects.filter(list_id=pk)
#         serializer = TodoModelSerializer(todos, many=True)
#         return render(request, "todos_list.html", {"todos": serializer.data, "todo_list": todo_list})
#
#
# class TodoAPIView(APIView):
#     permission_classes = (IsAuthenticated, )
#
#     def get_object(self, id):
#         try:
#             return TodoList.objects.get(name=id)
#         except TodoList.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def get(self, request, id):
#         todo_list = self.get_object(id)
#         completed_todos = Todo.objects.filter(list_id=id, category='Completed')
#         serializer = TodoModelSerializer(completed_todos, many=True)
#         return render(request, "completed_todos_list.html", {"todos": serializer.data, "todo_list": todo_list})
#
#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LAB4 Views

# def all_todos(request):
#     todos = Todo.objects.all()
#     return render(request, "todos_list.html", {"todos": todos})
#
#
# def todos_list(request, pk):
#     todos = Todo.objects.filter(category='Incomplete', list_id=pk)
#     todo_list = TodoList.objects.get(id=pk)
#     return render(request, "todos_list.html", {"todos": todos, "todo_list": todo_list})
#
#
# def completed_todos_list(request, id):
#     completed_todos = Todo.objects.filter(list_id=id, category='Completed')
#     todo_list = TodoList.objects.get(id=id)
#     return render(request, "completed_todos_list.html", {"todos": completed_todos, "todo_list": todo_list})
