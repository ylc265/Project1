from django.conf.urls import patterns, include, url
from django.contrib import admin
import frontpage.views as views1
import frontpage_users.views as views2
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'courses', views1.StudentCourseViewSet)
router.register(r'users', views2.UserViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nyumentor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^frontpage/', include('frontpage.urls', namespace='frontpage')),
    url(r'^frontpage_users/', include('frontpage_users.urls', namespace='users')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^search/', include('haystack.urls')),
)
