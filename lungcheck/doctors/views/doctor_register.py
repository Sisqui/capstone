from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from json import dumps
from datetime import datetime

def first_page(request) :
	context = {}
	context["message"] = "Please, provide us some basic information."
	context["first"] = True
	return render(request, 'doctors/auth/register_doctor.html', context)

def second_page(request) :
	context = {}
	# Get form data and merge it with old data
	new_data = dict(request.POST.lists())
	request.session["first_name"] = new_data["first_name"]
	request.session["last_name"] = new_data["last_name"]
	request.session["hospital"] = new_data["hospital"]
	request.session["license"] = new_data["license"]

	now = datetime.now()
	context["message"] = "Could you give us some more information?"
	context["second"] = True
	context["years"] = reversed(range(now.year-100, now.year-20))
	return render(request, 'doctors/auth/register_doctor.html', context)

def third_page(request, error="", error_code=0) :
	context = {}
	# Get form data and merge it with old data
	new_data = dict(request.POST.lists())
	request.session["birth_year"] = new_data["birth_year"]
	request.session["gender"] = new_data["gender"]
	request.session["country"] = new_data["country"]

	if error :
		context["error"] = error
		context["error_code"] = error_code
	else :
		context["message"] = "Finally, choose a username and password."

	context["third"] = True
	return render(request, 'doctors/auth/register_doctor.html', context)

def field_errors(data) :

	# Check if username exists
	if User.objects.filter(username=data['username']).exists() :
		return "Username already exists.", 1

	return "", ""

def register_user(request) :
	
	# Get new data
	new_data = dict(request.POST.lists())
	username = new_data["username"][0]
	password = new_data["password"][0]
	mail = new_data["mail"][0]

	# Check the data
	error, error_code = field_errors(new_data)
	if error :
		return third_page(request, error, error_code)
	
	# If corrent create new user
	User.objects.create_user(username, email=mail, password=password)
	return HttpResponse(request.session["first_name"])


# Doctor register
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

def json_user(user) : 
	userdata = {
			"username": user.username,
			"first_name": user.first_name,
			"last_name" : user.last_name,
			"mail" : user.email,
			"is_active" : user.is_active,
			"last_login" : user.last_login,
			"id" : user.id,
		}
	jsondata = dumps(userdata)
	return HttpResponse(jsondata, content_type='application/json')

# API sign up for app
@csrf_exempt
def api_register(request) :

	if request.POST and request.method == 'POST' :
		if not 'username' in request.POST :
			return json_error("No username given")
		if not 'password' in request.POST :
			return json_error("No password given")
		if not 'mail' in request.POST :
			return json_error("No mail given")

		# Get data
		data = dict(request.POST.lists())
		username = data["username"][0]
		password = data["password"][0]
		mail = data["mail"][0]

		# Check the data
		# TODO
		
		# If corrent create new user
		newuser = User.objects.create_user(username, email=mail, password=password)		
		return json_user(newuser)

	else :
		return json_error("No POST")

# API sign in for app
@csrf_exempt
def api_login(request) :

	if request.POST and request.method == 'POST' :
		if not 'username' in request.POST :
			return json_error("No username given")
		if not 'password' in request.POST :
			return json_error("No password given")

		# Get data
		data = dict(request.POST.lists())
		username = data["username"][0]
		password = data["password"][0]

		# Check the data
		# TODO
		
		# If corrent create new user
		user = authenticate(username=username, password=password)
		if user :
			# login(request, user)
			return json_user(user)
		else :
			return json_error("Incorrect login credentials")
		

	else :
		return "NO POST"