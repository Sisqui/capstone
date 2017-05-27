from django.contrib.auth.models import User
from django.db import models

#
# Doctor class
#	Extend the default user class
#	Add hospital and license
#	Needs to be manually validated by staff
#
class Doctor(models.Model) :

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
	birth_year = models.IntegerField(
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
	hospital = models.CharField(
		max_length=100, 
		null=True, 
		blank=True
	)
	license = models.CharField(
		max_length=100,
		null=True,
		blank=True
	)
	mail_code = models.CharField(
		max_length=20,
		null=True,
		blank=True
	)
	mail_confirmed = models.BooleanField(
		default=False
	)
	validated = models.BooleanField(
		default=False
	)

	def __str__ (self) :
		return "{} - {}".format(
					self.user.get_full_name, 
					self.license)