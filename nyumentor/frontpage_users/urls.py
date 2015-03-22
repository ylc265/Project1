from django.conf.urls import patterns, url 
from frontpage_users import views 

urlpatterns = patterns('',
	url(r'^user_profile/$', views.user_profile, name='profile'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
)