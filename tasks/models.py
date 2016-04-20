from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
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
	attribute_1 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_2 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_3 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_4 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_5 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_6 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_7 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_8 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_9 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
	attribute_10 = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('task', kwargs={'pk': self.pk})