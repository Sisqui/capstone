from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from  django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .doctor_intranet import doctor_intranet

# User confirm mail
def confirm_mail(request) :
	uid = request.GET.get('uid')
	code = request.GET.get('code')

	try :
		user = User.objects.get(id=uid)
	except ObjectDoesNotExist :
		raise Http404("User does not exist")

	try :
		if user.patient.mail_code == code :
			user.patient.mail_confirmed = True
			user.patient.save()
			login(request, user)
			return redirect(doctor_intranet)

	except ObjectDoesNotExist :
		if user.doctor.mail_code == code :
			user.doctor.mail_confirmed = True
			user.doctor.save()
			login(request, user)
			return redirect(doctor_intranet)
