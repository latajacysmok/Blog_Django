from django.conf.urls import url, include
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<page>\d+)', views.index, name="index"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^add_new_post/$', views.add_new_post, name="add_new_post"),
    url(r'^add_new_tag/$', views.add_new_tag, name="add_new_tag"),
    url(r'^edit_post/(?P<id>\d+)$', views.edit_post, name="edit_post"),
    url(r'^tag/(?P<name>\w+)/$', views.tag_view, name="tag_view"),
    url(r'^profile/(?P<id>\d+)/$', views.view_profile, name="view_profile"),
    url(r'^post/(?P<name>\w+)/$', views.post_view, name="post_view"),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^add_new_comment/(?P<id>\d+)/$', views.add_new_comment, name="add_new_comment"),
    url(r'^add_like/(?P<id>\d+)/$', views.add_like, name="add_like"),
    url(r'^del_like/(?P<id>\d+)/$', views.del_like, name="del_like"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^messages/', include('msgs.urls')),
    url(r'^api/', include('api.urls')),
]
