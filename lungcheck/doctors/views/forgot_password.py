from django.shortcuts import render, redirect

# User forgot password
def forgot_password(request) :
	# TODO
	if request.user.is_authenticated and request.user.doctor :
		return redirect(doctor_intranet)
	elif request.user.is_authenticated and request.user.patient :
		return redirect(patient_intranet)
	else :
		return render(request, 'doctors/auth/forgot_password_doctor.html')