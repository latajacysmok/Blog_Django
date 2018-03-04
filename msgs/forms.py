from django import forms
from .models import  Message

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['title', 'content', 'recipient']
		widgets = {
			'content': forms.Textarea(attrs={'cols': 30 , 'rows': 20})
		}
		labels = {
			'title': 'Tytul',
			'content': 'Zawartosc'
		}