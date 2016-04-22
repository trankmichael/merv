from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rating, CosineTaskSimilarity
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user','task', 'task_pk', 'score')

class CosineSimilarityAdmin(admin.ModelAdmin):
	list_display = ('user', 'task', 'similarity')

admin.site.register(Rating, RatingAdmin)
admin.site.register(CosineTaskSimilarity, CosineSimilarityAdmin)