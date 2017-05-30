from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404

import doctors

from json import dumps
from datetime import datetime

# Doctor login
def doctor_login(request) :

	if request.user.is_authenticated :
		try :
			if request.user.doctor :
				return redirect(doctors.views.doctor_intranet)
		except :
			pass

	if request.method and request.method == 'POST' :
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		
		if user :
			login(request, user)
			return redirect(doctors.views.doctor_intranet)
		else :
			context = {}
			context['error'] = "Incorrect username and/or password"
			return render(request, 'doctors/auth/login_doctor.html', context)
	else :
		return render(request, 'doctors/auth/login_doctor.html')

# Json error for api page
def json_error(error_code) :
	err = dumps({"ERROR" : error_code})
	return HttpResponse(err, content_type='application/json')

# API sign in for app
@csrf_exempt
def api_login(request) :

	if request.POST and request.method == 'POST' :
		if not 'username' in request.POST :
			return json_error("No username given")
		if not 'password' in request.POST :
			return json_error("No password given")

		# Get data
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Authenticate and login
		user = authenticate(username=username, password=password)
		if user and user.doctor :
			login(request, user)
			return HttpResponse(user.doctor.json(), content_type='application/json')
		else :
			return json_error("Incorrect login credentials for doctor")
		

	else :
		return json_error("No post")