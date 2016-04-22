from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rating
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user','task', 'task_pk', 'score')

admin.site.register(Rating, RatingAdmin)