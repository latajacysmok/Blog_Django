from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title  = models.CharField(max_length=200)
	content = models.CharField(max_length=10000)
	publish_date = models.DateField()
	# relacja 1 do wielu
	user = models.ForeignKey(User)
	class Meta:
		ordering = ['publish_date']

	def __str__(self):
		return "Tytuł postu: " + self.title + "\n Treść: " + self.content[:self.content.find('.')] + "..." \
		+ "\nData: " + self.publish_date.strftime("%d.%m.%Y") + "\nAutor:" + self.user.username

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "Tag o nazwie " + self.name

class PostToTag(models.Model):
	post = models.ForeignKey(Post)
	tag = models.ForeignKey(Tag)

	class Meta:
		unique_together = ('post', 'tag', )

	def __str__(self):
		return self.post.__str__() + " : " + self.tag.__str__()

# class Profile(models.Model):
# 	user = models.OneToOneField(User, cascade=True)
# 	o_mnie(null=True)
# 	adress
# 	avatar