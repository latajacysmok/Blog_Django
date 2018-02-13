from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<username>\w+)/$', views.UserDetail.as_view()),
]