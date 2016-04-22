from __future__ import unicode_literals

from django.db import models
from accounts.models import User 
from tasks.models import Task

# Create your models here.
class Rating(models.Model):
    """A Vote on a Product"""
    user = models.ForeignKey(User, related_name='ratings')
    task = models.ForeignKey(Task)
    # task_pk = models.ForeignKey(Task)
    task_pk = models.IntegerField()
    score = models.FloatField()

    def __str__(self):
        return "Rating"

class Recommendation(models.Model):
	user = models.ForeignKey(User, related_name='recommended')
	task = models.ForeignKey(Task)
	task_pk = models.IntegerField()
	predicted_score = models.FloatField()

class CosineTaskSimilarity(models.Model):
    user = models.ForeignKey(User, related_name='cosine')
    task = models.IntegerField()
    similarity = models.FloatField()