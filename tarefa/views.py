from rest_framework import viewsets
from .models import Task, User
from .serializer import TaskSerializer, UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer