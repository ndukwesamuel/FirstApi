from django.contrib import admin

# Register your models here.
from Todo.models import Task


admin.site.register(Task)
