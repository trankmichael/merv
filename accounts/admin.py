from django.contrib import admin
from tasks.models import Task
from accounts.models import User
# Register your models here.
admin.site.register(Task)
admin.site.register(User)
