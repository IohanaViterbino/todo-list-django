from rest_framework import serializers
from .models import Task, User, Comment, Tag, Notification, Attachment

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
	user = UserSerializer(source= 'fk_user',read_only=True)

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
	user = UserSerializer(source='fk_user', read_only=True)
	class Meta:
		model = Comment
		fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
	user = UserSerializer(source='fk_user', read_only=True)
	class Meta:
		model = Notification
		fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
	user = UserSerializer(source='fk_user', read_only=True)
	task = TaskSerializer(source='fk_task', read_only=True)
	class Meta:
		model = Attachment
		fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['fk_user', 'comment_text', 'fk_task']

class TagListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['tag_name']