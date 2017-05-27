from django.contrib.auth.models import User
from django.db import models

from .patient import Patient

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