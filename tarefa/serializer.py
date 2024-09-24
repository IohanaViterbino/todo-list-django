from rest_framework import serializers
from .models import Task, User, Comment, Tag

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)

	class Meta:
		model = Task
		fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
	# Serializa as tarefas relacionadas
	tasks = TaskSerializer(many=True, read_only=True)

	class Meta:
		model = Tag
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	tasks = TaskSerializer(source='fk_task', read_only=True)
	class Meta:
		model = Comment
		fields = '__all__'