from django.contrib.auth.models import User
from django.db import models

import uuid

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

#
# Path to store the recordings
#
# def audio_path(instance, filename) :


# Recording class
#	Is a set of 8 recordings
#	Has a patient assigned and the recorded time
#
class Recording(models.Model) :
	patient = models.ForeignKey(Patient)
	created = models.DateField(auto_now_add=True)
	sound_one = models.FileField()
	sound_two = models.FileField()
	sound_three = models.FileField()
	sound_four = models.FileField()
	sound_five = models.FileField()
	sound_six = models.FileField()
	sound_seven = models.FileField()
	sound_eight = models.FileField()


# Evaluation class
#	Is the evaluation of a recording
#	Includes the recording ID
#	wether the result is healthy or not
#	and the report of the evaluation
#
class Evaluation(models.Model) :
	recording = models.OneToOneField(Recording)
	healthy = models.BooleanField()
	report = models.TextField(null=True, blank=True)
