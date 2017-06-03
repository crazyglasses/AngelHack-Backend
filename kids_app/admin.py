# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ParentMap
from django.contrib import admin

# Register your models here.
class ResortAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(ParentMap)
