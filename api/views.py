from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, PostSerializer
from blog.models import Post, Tag, Comment, Profile
from django.contrib.auth.models import User

class UserList(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		print(request.data)
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		pass

class EntryList(APIView):
	def get(self, request, format=None):
		entries = Post.objects.all()
		serializer = PostSerializer(entries, many=True)
		return Response(serializer.data)

class UserDetail(APIView):
	def get(self, request, username, format=None):
		user = User.objects.get(username=username)
		serializer = UserSerializer(user)
		return Response(serializer.data)

class View():

	def as_view():
		return HttpResponse()