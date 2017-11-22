from django import forms
from .models import Post, Tag

class PostForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		choices = tuple([(tag.name, tag.name) for tag in Tag.objects.all()])
		self.fields['tags'] = forms.MultipleChoiceField(
			widget=forms.CheckboxSelectMultiple,
			choices=choices)

	title = forms.CharField(max_length=100, label="Title")
	content = forms.CharField(widget=forms.Textarea, max_length=1000, label="Text")
	