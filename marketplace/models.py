# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Story(models.Model):

	headline = models.CharField(max_length=50)
	article = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='images', blank=True, null=True)

	def __unicode__(self):
		return self.headline