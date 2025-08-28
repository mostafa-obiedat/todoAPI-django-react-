from rest_framework import serializers
from .models import Todo
from accounts.models import CustomUser

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'author', 'title', 'body', 'attachment')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')       