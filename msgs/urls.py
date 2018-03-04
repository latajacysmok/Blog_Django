from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^sendmessage/$', views.send_message, name="sendmessage"),
	url(r'^inbox/$', views.inbox, name="inbox"),
]