from django.shortcuts import render, redirect
from django.http import Http404


# Patient intranet with all the recordings
def patient_intranet(request) :

	if request.user.is_authenticated :
		try :
			if request.user.patient :
				return render(request, 'doctors/intranet/patient.html')
		except :
			return Http404("Page does not exist.")
	else :
		return redirect(patient_login)