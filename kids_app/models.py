# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django_mysql.models import ListCharField

from django.contrib.auth.models import User
# Create your models here.
import os
from django.conf import settings


class ParentMap(models.Model):
	parent= models.ForeignKey(User)
	mapName= models.CharField(max_length= 300,primary_key=True)
	no_of_ques= models.IntegerField()
	def __str__(self):
		return self.mapName
class QnA(models.Model):
	maps = models.ForeignKey(
    ParentMap,
    on_delete=models.CASCADE,
    verbose_name="mapName",)
	question= models.CharField(max_length=1000)
	hint= models.CharField(max_length=1000)
	ques_no= models.IntegerField()
	#tags= models.ListCharField(base_field=CharField(max_length=100), size=None, **kwargs)
	tags= models.CharField(max_length=1000)
	def setfoo(self, x):
		self.tags = json.dumps(x)
	def getfoo(self):
		return json.loads(self.tags)


# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.username, filename)

class Save_an_incoming_image(models.Model):
	image = models.ImageField(upload_to='images/', blank=True, null=True)