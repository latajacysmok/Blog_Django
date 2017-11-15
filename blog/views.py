from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Post, Tag, PostToTag, User
from .forms import PostForm
# Create your views here.
def index(request, page=1):
	print(page)
	posts = Post.objects.all()
	for post in posts:
		post.tags = []
	ptts = PostToTag.objects.all()
	for ptt in ptts:
		for post in posts:
			if ptt.post == post:
				post.tags.append(ptt.tag)
	context = {
		'posts' : posts
	}
	return render(request, 'blog/index.html', context)

def add_new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			tags = form.cleaned_data['tags']
			publish_date = datetime.datetime.now()
			post = Post(title=title, content=content, publish_date=publish_date, user=request.user)
			post.save()
			for name in tags:
				tag = Tag.objects.get(name=name)
				ptt = PostToTag(tag=tag, post=post)
				ptt.save()
			return HttpResponseRedirect('/')
	form = PostForm()
	context = {
		"form": form
	}
	return render(request, 'blog/add_new_post.html', context)

def tag_view(request, name):
	tag = Tag.objects.get(name=name)
	posts = [ptt.post for ptt in PostToTag.objects.filter(tag=tag)]
	for post in posts:
		post.tags = []
	ptts = PostToTag.objects.all()
	for ptt in ptts:
		for post in posts:
			if ptt.post == post:
				post.tags.append(ptt.tag)
	context = {
		'posts' : posts,
		'tagname' : tag.name
	}
	return render(request, 'blog/tag_view.html', context)

def user_name(request, name):
	profile = User.objects.get(username=name)
	posts = Post.objects.filter(user=profile)
	print(posts)
	context = {
		'profile': profile,
		'posts': posts
	}
	return render(request, 'blog/user_name.html', context)

def post_view(request,name):
	return render(request, 'blog/post_view.html')
