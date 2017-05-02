from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from datetime import datetime


# Doctor register
def doctor_register(request) :
	
	context = {}

	# GOTO next step
	if request.POST and request.method == 'POST' :
		# FINISHED
		if 'username' in request.POST :
			return HttpResponse("Registrating...")
		# GOTO third step
		elif 'experience' in request.POST :
			context["message"] = "Finally, choose a username and password."
			context["third"] = True
		# GOTO second step
		elif 'license' in request.POST :
			now = datetime.now()
			context["message"] = "Could you give us some more information?"
			context["second"] = True
			context["years"] = reversed(range(now.year-100, now.year-20))
		
	# First time in
	else :
		context["message"] = "Please, provide us some basic information."
		context["first"] = True

	return render(request, 'doctors/auth/register_doctor.html', context)