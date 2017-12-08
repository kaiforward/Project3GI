# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Mine, Upgrade

# Register your models here.
admin.site.register(Mine)
admin.site.register(Upgrade)