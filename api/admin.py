from django.contrib import admin
from api.models import TaskList, TaskItem

admin.site.register(TaskList)
admin.site.register(TaskItem)