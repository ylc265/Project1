from django.conf.urls import patterns, url 
from frontpage import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^professors/$', views.get_prof, name='professors'),
	url(r'^courses/(?P<course_slug>[\w\-]+)/$', views.get_cpage, name='course_info'),
	url(r'^professors/(?P<prof_slug>[\w\-]+)/$', views.get_prof, name='prof_info'),
	url(r'^add_course/$', views.add_course, name='add_course'),
)