from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import Http404

# Doctor login
def doctor_login(request) :

	if request.user.is_authenticated :
		if request.user.doctor :
			return redirect(doctor_intranet)

	if request.method and request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user :
			login(request, user)
			return redirect(doctor_intranet)
		else :
			# Incorrect details TODO
			return render(request, 'doctors/auth/login_doctor.html')
	else :
		return render(request, 'doctors/auth/login_doctor.html')

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

# Doctor register
def doctor_register(request) :
	# TODO
	return render(request, 'doctors/auth/register_doctor.html')

# Patient register
def patient_register(request) :
	# TODO
	return render(request, 'doctors/auth/register_patient.html')

# Doctor forgot password
def doctor_forgot_password(request) :
	# TODO
	if request.user.is_authenticated :
		return redirect(doctor_intranet)
	else :
		return render(request, 'doctors/auth/forgot_password_doctor.html')

# Patient forgot password
def patient_forgot_password(request) :
	# TODO
	if request.user.is_authenticated :
		return redirect(doctor_intranet)
	else :
		return render(request, 'doctors/auth/forgot_password_patient.html')

# Doctor intranet
def doctor_intranet(request) :
	
	if request.user.is_authenticated :
		if request.user.doctor :
			return render(request, 'doctors/intranet/doctor.html')
		else :
			return Http404("Page does not exist.")

	else :
		return redirect(doctor_login)

# Patient intranet with all the recordings
def patient_intranet(request) :

	if request.user.is_authenticated :
		if request.user.patient :
			return render(request, 'doctors/intranet/patient.html')
		else :
			return Http404("Page does not exist.")

	else :
		return redirect(patient_login)

# API patient login
def api_patient_login(request) :
	context = RequestContext(request)

	'''
	if request.Method == 'POST' :
		username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)

    	if user and user.is_active and user.patient > 0 :
    		login(request, user)
    		return HttpResponse("Hello patient")

	   	else :
	   		return HttpResponseRedirect('/')

	else :
		return HttpResponse("Invalud username or password")
	'''




