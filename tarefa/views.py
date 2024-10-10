from rest_framework import viewsets, generics
from .models import Task, Comment, Tag, Notification, Attachment
from .serializer import (
	TaskSerializer, CommentSerializer, TagSerializer, NotificationSerializer, AttachmentSerializer,
	CommentListSerializer, TagListSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class TaskRetrieveView(generics.RetrieveAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class AttachmentViewSet(viewsets.ModelViewSet):
	queryset = Attachment.objects.all()
	serializer_class = AttachmentSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class CommentListView(generics.ListAPIView):
	''' lista de comentários por tarefa '''
	serializer_class = CommentListSerializer
	def get_queryset(self):
		queryset = Comment.objects.filter(fk_task=self.kwargs['pk'])
		return queryset
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class TagListView(generics.ListAPIView):
	''' lista de tags por tarefa '''
	serializer_class = TagListSerializer
	def get_queryset(self):
		queryset = Tag.objects.filter(tasks=self.kwargs['pk'])
		return queryset
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]