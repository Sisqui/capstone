from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Patient login
def patient_login(request) :

	if request.method and request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user :
			login(request, user)
			return redirect(patient_intranet)
		else :
			# Incorrect details TODO
			return render(request, 'doctors/auth/login_patient.html')
	else :
		return render(request, 'doctors/auth/login_patient.html')

# API sign in for app
@csrf_exempt
def patient_api_login(request) :

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
		if user and user.patient :
			login(request, user)
			return HttpResponse(user.patient.json(), content_type='application/json')
		else :
			return json_error("Incorrect login credentials for patient")
		

	else :
		return json_error("No post")