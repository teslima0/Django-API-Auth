from django.contrib import admin
from .models import Task
# Register your models here.
from .models import Project
admin.site.register(Project)
admin.site.register(Task)