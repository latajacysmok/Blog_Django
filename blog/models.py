from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=1000, null=True)
	avatar = models.ImageField(upload_to='blog/static/blog/imgs/', default='blog/static/blog/imgs/default.svg')

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
		return "Tytul postu: " + self.title + "\n Tresc: " + self.content[:self.content.find('.')] + "..." \
		+ "\nData: " + self.publish_date.strftime("%d.%m.%Y") + "\nAutor:" + self.user.username

	def likes_count(self):
		likes = Like.objects.filter(post=self)
		return len(likes)

	def user_likes(self):
		likes = Like.objects.filter(post=self)
		return [l.user for l in likes]

	def likes_text(self):
		count = self.likes_count()
		if count == 0:
			return "0 osób lubi to"
		elif count == 1:
			return "1 osoba lubi to"
		elif count >= 2 and count <= 4:
			return str(count) + " osoby lubią to"
		else:
			return str(count) + " osób lubi to"



class Comment(models.Model):
	content = models.CharField(max_length=300)
	post = models.ForeignKey(Post)

class Like(models.Model):
	post  = models.ForeignKey(Post)
	user = models.ForeignKey(User)

	class Meta:
		unique_together = ('post', 'user')