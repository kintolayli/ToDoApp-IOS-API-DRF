from rest_framework import viewsets
from rest_framework import permissions

from .models import Todo, User

from .serializers import TodoSerializer, UserSerializer
from .permissions import Author


class TodoViewSet(viewsets.ModelViewSet):
    """
    Предоставляет API для модели Todo, которая позволяет 
    создавать, изменять и удалять записи. 
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (Author, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
