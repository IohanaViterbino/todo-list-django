from rest_framework import viewsets, generics
from .models import Task, Comment, Tag, Notification, Attachment
from .serializer import (
	TaskSerializer, CommentSerializer, TagSerializer, NotificationSerializer, AttachmentSerializer,
	CommentListSerializer
)
class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class TaskRetrieveView(generics.RetrieveAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class NotificationViewSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
	queryset = Attachment.objects.all()
	serializer_class = AttachmentSerializer

class CommentListView(generics.ListAPIView):
	''' lista de comentários por tarefa '''
	serializer_class = CommentListSerializer
	def get_queryset(self):
		queryset = Comment.objects.filter(fk_task=self.kwargs['pk'])
		return queryset