from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Message(models.Model):
	recipient = models.ForeignKey(User, related_name='recipient')
	sender = models.ForeignKey(User, related_name='sender')
	title = models.CharField(max_length= 100, blank=True, default='')
	content = models.CharField(max_length=300, blank=True, default='')
	message_date = models.DateTimeField(null=True)
	readed = models.BooleanField(default=False)

	def __str__(self):
		return self.title