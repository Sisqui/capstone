from django.contrib.auth.models import User
from django.db import models

from .doctor import Doctor

#
# Patient class
#	Extends the default user class
#	Has a doctor and last_active date to order in the intranet
#
class Patient(models.Model) :

	MALE = 'M'
	FEMALE = 'F'
	NOT_GIVEN = 'O'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(NOT_GIVEN, 'Not given'),
	)

	user = models.OneToOneField(
		User, 
		on_delete=models.CASCADE
	)
	doctor = models.ForeignKey(
		Doctor, 
		null=True, 
		blank=True,
	)
	age = models.IntegerField(
		null=True, 
		blank=True,
	)
	gender = models.CharField(
		max_length=1,
		choices=GENDER_CHOICES,
		default='O',
	)
	country = models.CharField(
		max_length=30, 
		null=True, 
		blank=True,
	)
	last_active = models.DateField(
		null=True, 
		blank=True,
	)

	def __str__ (self) :
		return user.get_full_name