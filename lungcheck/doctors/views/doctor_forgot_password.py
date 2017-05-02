from django.shortcuts import render, redirect

# Doctor forgot password
def doctor_forgot_password(request) :
	# TODO
	if request.user.is_authenticated :
		return redirect(doctor_intranet)
	else :
		return render(request, 'doctors/auth/forgot_password_doctor.html')