from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login

import doctors

# Doctor intranet
def doctor_intranet(request) :
	
	if request.user.is_authenticated :
		try :
			doctor = request.user.doctor
			if not doctor.mail_confirmed :
				context = {}
				context['page_title'] = "Doctor intranet"
				context['type'] = "danger"
				context['title'] = "Error"
				context['message'] = 'You need to validate your mail before proceeding.'
				return render(request, 'doctors/notification.html', context)
			elif not doctor.validated :
				context = {}
				context['page_title'] = "Doctor intranet"
				context['type'] = "warning"
				context['title'] = "Error"
				context['message'] = 'Your account needs to be validated by our team before proceeding.'
				return render(request, 'doctors/notification.html', context)
			else :
				return render(request, 'doctors/intranet/doctor.html')

		except :
			raise Http404("Page does not exist.")
	else :
		return redirect(doctors.views.doctor_login)