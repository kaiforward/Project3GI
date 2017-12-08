# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PlanetType, Planet, PlanetStorage
# Register your models here.
admin.site.register(PlanetType)
admin.site.register(Planet)
admin.site.register(PlanetStorage)

