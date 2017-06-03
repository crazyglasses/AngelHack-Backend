# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import mymethods
# Create your views here.
from django.http import HttpResponse,JsonResponse

from django.core import serializers

def index(request):
	user_name= request.GET.get("username",None)
	if user_name != None:
		maps= mymethods.getcall(user_name)
		data = serializers.serialize("json", maps)
		context = {'data' : data}
		return JsonResponse(context,safe=False)
	
def getQues(request):
	map_name= request.GET.get("mapname",None)
	if map_name != None:
		ques= mymethods.session_hit(map_name)
		ques_s = serializers.serialize("json", ques)
		ques_hint={'ques':ques_s}
		print ques_hint
		return JsonResponse(ques_hint, safe=False)
