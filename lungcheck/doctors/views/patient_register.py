from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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


# API sign up for app
@csrf_exempt
def patient_api_register(request) :

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

