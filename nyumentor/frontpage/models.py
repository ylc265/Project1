from django.db import models
from django.template.defaultfilters import slugify
from frontpage_users.models import UserProfile
# Create your models here.
'''
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

class CourseModel(models.Model):
	'''
	This is the model for the course and includes:
	- course prefix (example: Math_UA)
	- course number (example: 121)
	- course name   (example: Calculus I)
	- professor name
	'''
	# !!! Change course_prefix, course_number to just one field
	course_prefix = models.CharField(max_length=128)
	course_number = models.CharField(max_length=128)
	professor    = models.CharField(max_length=128)
	course_name   = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128)
	prof_slug = models.SlugField()
	# !!! I need one more field here for Fall/Spring year taken 


	def save(self, *args, **kwargs):
		self.slug = '{}-{}-{}-{}'.format(slugify(self.course_prefix), slugify(self.course_number), slugify(self.course_name),slugify(self.professor))
		self.prof_slug = slugify(self.professor)
		super(CourseModel, self).save(*args, **kwargs)

	def __str__(self):
		return self.course_prefix + ' ' + self.course_number + ' ' + self.professor

class StudentCourseModel(models.Model):
	'''
	This is the model for a student's experience with a course. Includes:
	- course_user  (example: UserProfile)
	- course       (example: CourseModel)
	- course_grade (example: A)
	- verified     (example: True)
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
	course_model = models.ForeignKey(CourseModel, null=True)
	course_grade  = models.CharField(max_length=128,
		choices=GRADE_CHOICES)
	verified = models.BooleanField(default=False)

	def __str__(self):
		return str(self.course_model) + ' ' + str(self.course_user)

