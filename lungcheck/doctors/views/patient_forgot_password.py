from django.shortcuts import render, redirect

# Patient forgot password
def patient_forgot_password(request) :
	# TODO
	if request.user.is_authenticated :
		return redirect(doctor_intranet)
	else :
		return render(request, 'doctors/auth/forgot_password_patient.html')