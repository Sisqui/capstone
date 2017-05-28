from django.contrib.auth.models import User
from django.db import models

from json import dumps

#
# Doctor manager
#	Create function that first creates the user
#
class DoctorManager(models.Manager) :
	def create_doctor(self, username, password, mail, first_name='', last_name='', birth_year='', gender='', country='', hospital='', license='') :
		auth_user = User.objects.create_user(
			username, 
			email=mail, 
			password=password,
			first_name=first_name,
			last_name=last_name
		)
		doctor = self.create(
			user=auth_user,
			birth_year=birth_year,
			gender=gender,
			country=country,
			hospital=hospital,
			license=license
		)
		return doctor

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

	objects = DoctorManager()

	def __str__ (self) :
		return "{} - {}".format(
					self.user.get_full_name, 
					self.license)

	#def clean(self) :

	def json(self) :
		data = {
			"user_id" : self.user.id,
			"username": self.user.username,
			"first_name": self.user.first_name,
			"last_name" : self.user.last_name,
			"mail" : self.user.email,
			"is_active" : self.user.is_active,
			"last_login" : self.user.last_login,
			
			"doctor_id" : self.id,
			"country" : self.country,
			"gender" : self.gender,
			"birth_year" : self.birth_year,
			"license" : self.license,
			"hospital" : self.hospital,
			"mail_code" : self.mail_code,
			"mail_confirmed" : self.mail_confirmed,
			"validated" : self.validated
		}
		return dumps(data)
