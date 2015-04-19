import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from registration.signals import user_activated
# Create your models here.

def user_activated_callback(sender, user, request, **kwargs):
	'''
	This allows me to create a UserProfile when a user is activate 
	for more information on signal, take a look at 
	https://docs.djangoproject.com/en/dev/topics/signals/#connecting-receiver-functions
	'''
	profile = UserProfile(user = user)
	profile.save()

user_activated.connect(user_activated_callback)

def get_path_name(instance, filename):
	return os.path.join(settings.STATIC_PATH, 'profile_images', filename)

class UserProfile(models.Model):
	'''
	This is the user profile model which a user can modify and look 
	at his/her information.
	'''
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to=get_path_name, blank=True)
	#courses = models.ManyToManyField(CourseModel)

	def __str__(self):
		return self.user.username
