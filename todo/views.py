from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins

from .models import Todo, User

from .serializers import TodoSerializer, UserSerializer
from .permissions import Author, IsUser


class TodoViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    """
    Предоставляет API для модели Todo, которая позволяет 
    создавать, изменять и удалять записи. 
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (Author, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsUser, )