from django.contrib.auth.models import User
from django.db import models

from .recording import Recording

# Evaluation class
#	Is the evaluation of a recording
#	Includes the recording ID
#	wether the result is healthy or not
#	and the report of the evaluation
#
#	checked to know if the doctor listened to it
#	doctor_review to see if the doctor thin
#
class Evaluation(models.Model) :
	recording = models.OneToOneField(Recording)
	healthy = models.NullBooleanField(
		null=True,
		blank=True
	)
	report = models.TextField(
		null=True, 
		blank=True
	)
	checked = models.NullBooleanField(
		null=True,
		blank=True
	)
	doctor_review = models.NullBooleanField(
		null=True,
		blank=True
	)
	doctor_comment = models.TextField(
		null=True,
		blank=True
	)


