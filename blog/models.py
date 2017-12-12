from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	about = models.CharField(max_length=1000, null=True)
	#avatar = models.ImageField(upload_to='media/', blank=True)

class Post(models.Model):
	title  = models.CharField(max_length=200)
	content = models.CharField(max_length=10000)
	publish_date = models.DateField(default=datetime.datetime.now)
	edit_date	= models.DateField(null=True)
	# relacja 1 do wielu
	user = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)
	class Meta:
		ordering = ['-publish_date']

	def __str__(self):
		return "Tytuł postu: " + self.title + "\n Treść: " + self.content[:self.content.find('.')] + "..." \
		+ "\nData: " + self.publish_date.strftime("%d.%m.%Y") + "\nAutor:" + self.user.username


