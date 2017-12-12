from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from .models import Post, Tag, User
from .forms import PostForm, OurSignupForm
from project.settings import POSTS_PER_PAGE
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request, page='1'):
	page = int(page)
	posts = Post.objects.all()
	startPost = (page-1) * POSTS_PER_PAGE
	endPost = page * POSTS_PER_PAGE
	if startPost > len(posts):
		raise Http404
	context = {
		'posts' : posts[startPost:endPost],
		'page' : page,
		'isFirst': (page == 1),
		'isLast': endPost >= len(posts),
		'nextPage': page+1,
		'prevPage': page-1,
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
			messages.success(request, 'Utworzył się nowy post o tytule {}'.format(title)) # wiadomość o nowym poście
			return HttpResponseRedirect('/')

	form = PostForm()
	context = {
		"form": form
	}
	return render(request, 'blog/add_new_post.html', context)

def edit_post(request, id):
	id = int(id)
	post = Post.objects.get(id=id)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post.title = form.cleaned_data['title'] 
			post.content = form.cleaned_data['content']
			post.edit_date = datetime.datetime.now()
			tags = form.cleaned_data['tags']
			post.save()
			# todo: tagi
			return HttpResponseRedirect('/')
	form = PostForm(initial={
		'title': post.title,
		'content': post.content,
		'tags': [(ptt, ptt) for ptt in PostToTag.objects.filter(post=post).values_list('tag', flat=True)]
	})
	context = {
		"form": form
	}
	return render(request, 'blog/edit_post.html', context)

def tag_view(request, name):
	tag = Tag.objects.get(name=name)
	posts = [ptt.post for ptt in PostToTag.objects.filter(tag=tag)]
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

def signup(request):
	if request.method == 'POST':
		form = OurSignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			# user = User(username=username, password=password, email=email)
			# user.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect('/')

	form = OurSignupForm()
	context = {
		'form': form
	}
	return render(request, 'registration/signup.html', context)

