from tarefa.views import (
    TaskViewSet, CommentViewSet, TagViewSet, TaskRetrieveView, NotificationViewSet, AttachmentViewSet,
    CommentListView, TagListView
)
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'attachments', AttachmentViewSet, basename='attachments')

urlpatterns = [
    path('', include(router.urls)),
    path('task/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
    path('task/<int:pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('task/<int:pk>/tags/', TagListView.as_view(), name='tag-list'),
]