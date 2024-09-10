from django.contrib import admin
from tarefa.models import Task
# Register your models here.

class tasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', ' description', ' created_at', 'due_date', ' completed' )
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Task, tasksAdmin)