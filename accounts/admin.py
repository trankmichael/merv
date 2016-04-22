from django.contrib import admin
from tasks.models import Task
from accounts.models import User
from recommender.models import Rating
# Register your models here.
# admin.site.register(Task)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)
