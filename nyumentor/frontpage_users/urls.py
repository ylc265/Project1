from django.conf.urls import patterns, url 
from frontpage_users import views 

urlpatterns = patterns('',
	url(r'^user_profile/$', views.user_profile, name='profile'),
)