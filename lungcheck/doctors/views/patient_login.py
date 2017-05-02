from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Patient login
def patient_login(request) :

	if request.method and request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user :
			login(request, user)
			return redirect(patient_intranet)
		else :
			# Incorrect details TODO
			return render(request, 'doctors/auth/login_patient.html')
	else :
		return render(request, 'doctors/auth/login_patient.html')