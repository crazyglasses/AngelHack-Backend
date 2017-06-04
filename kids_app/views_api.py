from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import os
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager as bum
from models import Save_an_incoming_image

def azure_call(file):
	########### Python 2.7 #############
	import httplib, urllib, base64, json
	import requests

	headers = {
	    # Request headers.
	    #Content-Type for image url
	    #'Content-Type': 'application/json',
	    
	    #Content-Type for raw image binary
	    'Content-Type': 'application/octet-stream',
	    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
	    'Ocp-Apim-Subscription-Key': '49ad35771351495e97da5c3f9db70b61',
	}

	params = urllib.urlencode({
	    # Request parameters. All of them are optional.
	    'visualFeatures': 'Categories, Tags, Description',
	    'details': 'Celebrities',
	    'language': 'en',
	})

	# Replace the three dots below with the URL of a JPEG image of a celebrity.
	#body = "{'url':'http://i.dailymail.co.uk/i/pix/2015/01/06/242CDF6C00000578-2899668-image-m-102_1420587021242.jpg'}"
	#body for image url
	#body = "{'url':'http://media.gettyimages.com/photos/security-guard-standing-in-front-of-gate-picture-id88621094?s=612x612'}"

	#body for image binary
	body= open(file, 'rb').read()

	try:
	    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
	    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the
	    #   URL below with "westus".
	    conn = httplib.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
	    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
	    response = conn.getresponse()
	    data = response.read()
	    parsed = json.loads(data)
	    #print parsed
	    print ("REST Response:")
	    final_data = (json.dumps(parsed, sort_keys=True, indent=4))
	    
	    print final_data
	    return final_data
	    print "closing"
	    conn.close()
	except Exception as e:
		print "error"
		print e
		pass


@csrf_exempt
def index(request):
	x = [a for a in range(0,10)]
	data = {
	'x' : x
	}

	if request.FILES:
		print "files received!"
		save_this_file = request.FILES.get('upload_file')
		username = request.user.username
		image_class = Save_an_incoming_image()
		image_class.image = save_this_file

		image_class.save()
		# print image_class, username
		# file_name = bum().make_random_password(32)
	# 	destination = open( + file_name + str(save_this_file), 'wb+')
	# 	print file_name
	# 	for chunk in save_this_file.chunks():
	# 		destination.write(chunk)
	# 	destination.close()
		print "callingAZ"
		return JsonResponse(azure_call(image_class.image.path), safe=False)	
	return HttpResponse("No file received :/")



