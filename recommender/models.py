from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Vote(models.Model):
    """A Vote on a Product"""
    user = models.ForeignKey(User, related_name='votes')
    task = models.ForeignKey(Product)
    score = models.FloatField()

    def __str__(self):
        return "Vote"