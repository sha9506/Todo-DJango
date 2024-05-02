from django.contrib import admin
from taskdo.models import Task
from taskdo.models import User
# Register your models here.

admin.site.register(Task)
admin.site.register(User)