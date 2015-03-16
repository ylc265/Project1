from django.db import models
from django.contrib.auth.models import User
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

class UserProfile(models.Model):
	'''
	This is the user profile model which a user can modify and look 
	at his/her information.
	'''
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	#courses = models.ManyToManyField(CourseModel)

	def __str__(self):
		return self.user.username
