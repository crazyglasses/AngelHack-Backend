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
		ques= mymethods.session_hit(map_name)[0]
		hint= mymethods.session_hit(map_name)[1]
		ques_s = serializers.serialize("json", ques)
		hint_s = serializers.serialize("json", hint)
		ques_hint={'ques':ques_s,'hint':hint_s}
		return JsonResponse(ques_hint, safe=False)
