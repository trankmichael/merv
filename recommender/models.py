from __future__ import unicode_literals

from django.db import models
from accounts.models import User 
from tasks.models import Task

# Create your models here.
class Ratings(models.Model)
    """A Vote on a Product"""
    user = models.ForeignKey(User, related_name='ratings')
    task = models.ForeignKey(Task)
    score = models.FloatField()

    def __str__(self):
        return "Vote"