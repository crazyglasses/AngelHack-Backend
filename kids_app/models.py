# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class detials(models.Model):
    map_name= models.CharField(max_length=200)
    object_i= models.CharField(max_length=200) 
    hint = models.CharField(max_length=200)

