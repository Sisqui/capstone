from django.shortcuts import render, redirect

# User forgot password
def forgot_password(request) :
	if request.user.is_authenticated and request.user.doctor :
		return redirect(doctor_intranet)
	elif request.user.is_authenticated and request.user.patient :
		return redirect(patient_intranet)
	else :
		context = {}
		if request.POST and request.method == 'POST' :
			# TODO send mail
			context['request'] = False
		else :
			context['request'] = True			
		return render(request, 'doctors/auth/password_recover_ask.html', context)

def new_password(request) :
	pass