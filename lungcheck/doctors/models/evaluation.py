from django.contrib.auth.models import User
from django.db import models

from .recording import Recording

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
