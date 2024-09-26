from tarefa.views import TaskViewSet, CommentViewSet, TagViewSet, TaskRetrieveView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('task/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
]