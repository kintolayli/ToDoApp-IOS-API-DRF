from rest_framework import serializers

import datetime as dt

from .models import Todo, User


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'name', 'is_completed', 'created')


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'todos')
        lookup_field = 'username'
        ref_name = 'ReadOnlyUsers'