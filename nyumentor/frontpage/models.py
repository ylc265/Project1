from django.db import models
from django.template.defaultfilters import slugify
from frontpage_users.models import UserProfile
# Create your models here.

class Category(models.Model):
	CATEGORY_CHOICES = (
		('MATH', 'Math'),
		('ENG', 'English'),
		('CS', 'Computer Science'),
	)
	name = models.CharField(max_length=128,
		choices=CATEGORY_CHOICES, unique=True)

	def __str__(self):
		# for a very strange reason, it's still __str__ and not 
		# __unicode__
		return self.name 

class CourseModel(models.Model):
	'''
	This is the model for the course and includes:
	- course prefix (example: Math_UA)
	- course number (example: 121)
	- course name   (example: Calculus I)
	- professor name
	'''
	
	GRADE_CHOICES = (
		('A', 'A'),
		('A-', 'A-'),
		('B+', 'B+'),
		('B', 'B'),
		('B-', 'B-'),
		('C+', 'C+'),
		('C', 'C'),
		('C-', 'C-'),
		('D+', 'D+'),
		('D', 'D'),
		('F', 'F'))
	course_user  = models.ForeignKey(UserProfile, null=True)
	category     = models.ForeignKey(Category)
	coursenumber = models.CharField(max_length=128)
	professor    = models.CharField(max_length=128)
	coursename   = models.CharField(max_length=128)
	slug = models.SlugField()
	prof_slug = models.SlugField()
	coursegrade  = models.CharField(max_length=128,
		choices=GRADE_CHOICES)
	# !!! I need one more field here for Fall/Spring year taken 


	def save(self, *args, **kwargs):
		self.slug = '{}-{}'.format(slugify(self.coursenumber), slugify(self.professor))
		self.prof_slug = slugify(self.professor)
		super(CourseModel, self).save(*args, **kwargs)

	def __str__(self):
		return self.coursenumber + ' ' + self.professor

