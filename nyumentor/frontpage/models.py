from django.db import models
from django.template.defaultfilters import slugify
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
'''
class CourseNumber(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name 

class Professor(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name 

class CourseName(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name 
'''
class CourseModel(models.Model):
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

