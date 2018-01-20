from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from .models import Post, Tag, User, Profile, Comment
from .forms import PostForm, OurSignupForm, ProfileForm, CommentForm
from project.settings import POSTS_PER_PAGE
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models.signals import post_save


def index(request, page='1'):
	page = int(page)
	posts = Post.objects.all()
	startPost = (page-1) * POSTS_PER_PAGE
	endPost = page * POSTS_PER_PAGE
	if startPost > len(posts):
		raise Http404
	for post in posts:
		post.comments = Comment.objects.filter(post=post)
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
			tags = form.cleaned_data['tags']
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			post.tags.add(*tags)
			post.save()
			messages.success(request, 'Utworzyl sie nowy post o tytule {}'.format(title))
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
			post.tags.clear()
			post.tags.add(*tags)
			post.save()
			# todo: tagi
			return HttpResponseRedirect('/')
	form = PostForm(initial={
		'title': post.title,
		'content': post.content,
		'tags': post.tags.all()
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
	profile = Profile.objects.get(user=request.user)
	posts = Post.objects.filter(user=request.user)
	# print(posts)
	context = {
		'profile': profile,
		'posts': posts
	}
	return render(request, 'blog/user_name.html', context)

def post_view(request, id):
	posts = get_object_or_404(Post, id=int(id))
	context = {
		'posts': posts
	}
	return render(request, 'blog/post_view.html', context)

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

def add_new_comment(request, id):
	post = Post.objects.get(id=int(id))
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			comment = Comment(post=post, content=content)
			comment.save()
			return HttpResponseRedirect('/')
	else:
		form = CommentForm()
		context = {
			'form': form,
			'post': post
		}
		return render(request, 'blog/add_new_comment.html', context)


def edit_profile(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.description = form.cleaned_data['description']
			profile.avatar = form.cleaned_data['avatar']
			profile.save()
			return HttpResponseRedirect('/')
	else:
		form = ProfileForm(initial={
			'description': profile.description,
		})
		context = {
			'form': form,
			'profile': profile
		}
		return render(request, 'blog/editprofile.html', context)

def create_profile(sender, **kwargs):
	user = kwargs['instance']
	if kwargs['created']:
		profile = Profile(user=user)
		profile.save()

post_save.connect(create_profile, sender=User)