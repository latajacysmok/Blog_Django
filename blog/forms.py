from django import forms
from .models import Post, Tag, Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		widgets = {
			'content': forms.Textarea(attrs={'cols': 40, 'rows': 15 })
		}
		fields = ['title', 'content', 'tags']	

class OurSignupForm(UserCreationForm):
	email = forms.EmailField(max_length=255, help_text="Podaj maila")

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['description', 'avatar']
		widgets = {
			'description': forms.Textarea(attrs={'cols': 30 , 'rows': 10})
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		widgets = {
			'content': forms.Textarea(attrs={'cols': 40, 'rows': 15 })
		}