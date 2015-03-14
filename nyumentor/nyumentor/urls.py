from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nyumentor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^frontpage/', include('frontpage.urls')),
    url(r'^frontpage_users/', include('frontpage_users.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
