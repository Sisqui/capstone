from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Doctor login
def doctor_login(request) :

	if request.user.is_authenticated :
		try :
			if request.user.doctor :
				return redirect(doctor_intranet)
		except :
			pass

	if request.method and request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user :
			login(request, user)
			return redirect(doctor_intranet)
		else :
			# Incorrect details TODO
			return render(request, 'doctors/auth/login_doctor.html')
	else :
		return render(request, 'doctors/auth/login_doctor.html')