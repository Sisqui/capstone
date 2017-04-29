from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='doctors/home/doctor.html'), name="doctor_home"),
	url(r'^patients$', TemplateView.as_view(template_name='doctors/home/patient.html'), name="patient_home"),
	url(r'^login/$', views.doctor_login, name="doctor_login"),
	url(r'^patients/login/$', views.patient_login, name="patient_login"),
	url(r'^register/$', views.doctor_register, name="doctor_register"),
	url(r'^patients/register/$', views.patient_register, name="patient_register"),
	url(r'^forgot_password/$', views.doctor_forgot_password, name="doctor_forgot_password"),
	url(r'^patients/forgot_password/$', views.patient_forgot_password, name="patient_forgot_password"),
	url(r'^intranet/$', views.doctor_intranet, name="doctor_intranet"),
	url(r'^patients/intranet/$', views.patient_intranet, name="patient_intranet"),
]

