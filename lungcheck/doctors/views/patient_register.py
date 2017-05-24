from django.shortcuts import render

from json import dumps
from datetime import datetime

# First register form
def first_page(request, error="", error_code="") :
	context = {}
	if error :
		context["error"] = error
		context["error_code"] = error_code
	else :
		context["message"] = "Now choose a username and password."
		now = datetime.now()
		context["years"] = reversed(range(now.year-100, now.year-2))
	context["message"] = "To start, provide us some basic information."
	context["first"] = True
	return render(request, 'doctors/auth/register_patient.html', context)

# Second register form
def second_page(request, error="", error_code=0) :
	context = {}
	# Get form data and merge it with old data
	new_data = dict(request.POST.lists())
	request.session["first_name"] = new_data["first_name"]
	request.session["last_name"] = new_data["last_name"]
	request.session["birth_year"] = new_data["birth_year"]
	request.session["gender"] = new_data["gender"]
	request.session["country"] = new_data["country"]

	if error :
		context["error"] = error
		context["error_code"] = error_code
	else :
		context["message"] = "Now choose a username and password."

	context["second"] = True
	return render(request, 'doctors/auth/register_patient.html', context)

def register_user(request) :
	
	# Get new data
	new_data = dict(request.POST.lists())
	username = new_data["username"][0]
	password = new_data["password"][0]
	mail = new_data["mail"][0]

	# Check the data
	error, error_code = field_errors(new_data)
	if error :
		return second_page(request, error, error_code)
	
	# If corrent create new user
	User.objects.create_user(username, email=mail, password=password)
	return HttpResponse(request.session["first_name"])

# Patient register
def patient_register(request) :
	
	# GOTO next step
	if request.POST and request.method == 'POST' :
		# FINISHED
		if 'username' in request.POST :
			return register_user(request)
		# Second step
		elif 'country' in request.POST :
			return second_page(request)
			
	# First time in
	return first_page(request)

