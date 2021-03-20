from rest_framework import viewsets
from rest_framework.response import Response
from .models import MainUserManager
from .serializers import UserSerializer


class Register(viewsets.ViewSet):
    def create(self, request):
        new_user = MainUserManager._create_user(self, 'kd@j.ru', '12345')
        serializer = UserSerializer(new_user)
        return Response(serializer.data)
