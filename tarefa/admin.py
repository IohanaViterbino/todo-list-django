from django.contrib import admin
from tarefa.models import Task

class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'due_date', 'completed' )
    list_filter = ['user', 'completed']
    list_display_links = ('id', 'title',)
    list_editable = ('completed',)
    search_fields = ('title',)
    list_per_page = 10

admin.site.register(Task, TasksAdmin)