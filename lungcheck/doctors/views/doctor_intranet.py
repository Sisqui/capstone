
# Doctor intranet
def doctor_intranet(request) :
	
	if request.user.is_authenticated :
		try :
			if request.user.doctor :
				return render(request, 'doctors/intranet/doctor.html')
		except :
			return Http404("Page does not exist.")
	else :
		return redirect(doctor_login)