# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import mymethods
# Create your views here.
from django.http import HttpResponse,JsonResponse

from django.core import serializers
from kids_app.models import ParentMap,QnA

from django.contrib.auth.decorators import login_required

@login_required
def Mapform(request):
	if request.POST:
		mapname= request.POST['MapName']
		noofques = request.POST['ques']
		user = request.user
		obj = ParentMap(parent = user, mapName = mapname , no_of_ques= noofques)
		obj.save()

		
	return render(request,'dashboard/mapform.html')

@login_required
def qform(request):
	if request.POST:
		mapname = request.POST['mapname']
		Map = ParentMap.objects.get(mapName = mapname)
		question = request.POST['question']
		hint = request.POST['hint']
 		qno = request.POST['qno']
		tags =request.POST['tags']
		qna = QnA(maps = Map,question = question,hint = hint,ques_no = qno,tags =tags)
		qna.save()

	map_names = ParentMap.objects.all()
	context = {"map_names": map_names}
	
	return render(request,'dashboard/questionform.html', context)

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

@login_required
def dashboard(request):
	user_name= request.user.username
	name = request.user.first_name + request.user.last_name
	context = {"name": name}
	return render(request, 'dashboard/index.html', context)