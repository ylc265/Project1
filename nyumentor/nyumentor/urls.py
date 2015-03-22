from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nyumentor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^frontpage/', include('frontpage.urls', namespace='frontpage')),
    url(r'^frontpage_users/', include('frontpage_users.urls', namespace='users')),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
