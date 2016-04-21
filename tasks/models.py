from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from scipy import spatial
# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Task(models.Model):

	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	task_name = models.CharField(_('task name'), max_length=30, blank=False, null=True)
	collaborative = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	strength = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	transportation = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	outdoor = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	language = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('task-detail', kwargs={'pk': self.pk})

class Scores(models.Model):
	key = models.FloatField()
	score = models.FloatField()
