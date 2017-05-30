from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

from ..models import Doctor

from json import dumps
from datetime import datetime

def first_page(request) :
	context = {}
	context["message"] = "Please, provide us some basic information."
	context["first"] = True
	return render(request, 'doctors/auth/register_doctor.html', context)

def second_page(request) :
	context = {}
	# Get form data and save in in the session
	new_data = dict(request.POST.lists())
	request.session["first_name"] = new_data["first_name"][0]
	request.session["last_name"] = new_data["last_name"][0]
	request.session["hospital"] = new_data["hospital"][0]
	request.session["license"] = new_data["license"][0]

	now = datetime.now()
	context["message"] = "Could you give us some more information?"
	context["second"] = True
	context["years"] = reversed(range(now.year-100, now.year-20))
	return render(request, 'doctors/auth/register_doctor.html', context)

def third_page(request, error="", error_code=0) :
	context = {}
	if error_code > 1 :
		context["username"] = request.POST.get('username', '')
	context["mail"] = request.POST.get('mail', '')

	if error :
		context["error"] = error
		context["error_code"] = error_code
	else :
		request.session["birth_year"] = request.POST.get("birth_year")
		request.session["gender"] = request.POST.get("gender")
		request.session["country"] = request.POST.get("country")
		context["message"] = "Finally, choose a username and password."

	context["third"] = True
	return render(request, 'doctors/auth/register_doctor.html', context)


def register_user(request) :
	
	username = request.POST.get('username')
	password = request.POST.get('password')
	confirm_password = request.POST.get('confirm_password')

	if len(username) < 4 :
		return third_page(
			request,
			error="Username must be at least 4 characters long", 
			error_code = 1)
	if len(password) < 8 :
		return third_page(
			request,
			error="Password must be at least 8 characters long",
			error_code = 2 )
	if password != confirm_password :
		return third_page(
			request,
			error = "Passwords do not match",
			error_code = 3)
	
	# Create a new doctor objec
	try :
		doctor = Doctor.objects.create_doctor(
			username = request.POST.get('username'),
			password = request.POST.get('password'),
			mail=request.POST.get('mail'),
			first_name = request.session['first_name'],
			last_name = request.session['last_name'],
			birth_year=request.session['birth_year'],
			gender=request.session['gender'],
			country=request.session['country'],
			hospital=request.session['hospital'],
			license=request.session['license']
		)
	except IntegrityError :
		return third_page(
			request,
			error="Username already in use",
			error_code = 1
		)

	# Save doctor
	doctor.save()

	# Authenticate and login


	# Redirect to intranet
	return redirect(doctor_intranet)


# Doctor register page
def doctor_register(request) :

	# GOTO next step
	if request.POST and request.method == 'POST' :
		# FINISHED
		if 'username' in request.POST :
			return register_user(request)
		# GOTO third step
		elif 'experience' in request.POST :
			return third_page(request)
		# GOTO second step
		elif 'first_name' in request.POST :
			return second_page(request)
			
	# First time in
	return first_page(request)

# Json error for api page
def json_error(error_code) :
	err = dumps({"ERROR" : error_code})
	return HttpResponse(err, content_type='application/json')

# API sign up for app
@csrf_exempt
def api_register(request) :

	if request.POST and request.method == 'POST' :

		if not 'username' in request.POST :
			return json_error("No username given")
		elif len(request.POST.get('username')) < 4 :
			return json_error("Username must be at least 4 characters long")

		if not 'password' in request.POST :
			return json_error("No password given")
		elif len(request.POST.get('password')) < 8 :
			return json_error("Password must be at least 8 characters long")

		if not 'mail' in request.POST :
			return json_error("No mail given")

		# Create a new doctor object
		try :
			doctor = Doctor.objects.create_doctor(
				username = request.POST.get('username'),
				password = request.POST.get('password'),
				mail=request.POST.get('mail'),
				first_name = request.POST.get('first_name', ''),
				last_name = request.POST.get('last_name', ''),
				birth_year=request.POST.get('birth_year', 0),
				gender=request.POST.get('gender', ''),
				country=request.POST.get('country', ''),
				hospital=request.POST.get('hospital', ''),
				license=request.POST.get('license', '')
			)
		except IntegrityError :
			return json_error("Username already exists")
		
		# If corrent create new user	
		doctor.save()

		# Authenticate and login to update last_login

		# Return data
		return HttpResponse(doctor.json(), content_type='application/json')

	else :
		return json_error("No POST")

