from rest_framework import generics
from .models import Todo
from accounts.models import CustomUser
from .permissions import IsAuthorOrReadOnly
from .serializers import TodoSerializer, UserSerializer
# Create your views here.

class ListTodo(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
