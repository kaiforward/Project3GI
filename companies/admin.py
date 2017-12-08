# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Company, CompanyStorage, CompanyTrade, Ownership, MineOwnership, PlanetTrade

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyStorage)
admin.site.register(CompanyTrade)
admin.site.register(PlanetTrade)
admin.site.register(Ownership)
admin.site.register(MineOwnership)