from django.contrib import admin
from todo.models import Task

class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'status', 'end_date', 'description',)
    
admin.site.register(Task, TodoAdmin)
