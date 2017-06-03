from . import models

from django.contrib.auth.models import User

def getcall(username):
	#uname= models.ParentMap.objects.get(parent)
	maps= models.ParentMap.objects.filter(parent__username=username)
	
	#if uname==username:
	#	maps= uname.giveMapname()
	#maps= models.ParentMap.objects.get(mapName)
	return maps

def session_hit(mapname):
	ques= models.QnA.objects.filter(maps__mapName=mapname)[0]
	hint= models.QnA.objects.filter(maps__mapname=mapname)[1]
	return ques,hints

