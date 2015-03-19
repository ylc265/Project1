import re
from django import forms 
from frontpage.models import StudentCourseModel, CourseModel 

course_prefix_pattern = re.compile(r'\w+-\w+', re.IGNORECASE)
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

class CourseForm(forms.Form):
	'''
	This is the form I am going to use to create both the CourseModel and the 
	StudentCourseModel
	'''
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	prof_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	course_prefix = forms.CharField(max_length=128, help_text="Enter Course Prefix: ")
	course_number = forms.CharField(max_length=128, help_text="Enter Course Number: ")
	professor    = forms.CharField(max_length=128, help_text="Enter Professor's Full Name: ")
	course_name   = forms.CharField(max_length=128, help_text="Enter Course's Name: ")
	course_grade  = forms.ChoiceField(help_text="Enter Grade Received: ", choices = GRADE_CHOICES)

	# !!! In the future, maybe regular expression for the input. For example, CS_UA, must always
	# follow a standard.
	def clean(self):
		cleaned_data = super(CourseForm, self).clean()
		course_prefix_valid = cleaned_data.get('course_prefix')
		if not course_prefix_pattern.match(course_prefix_valid):
			self._errors['course_prefix'] = self.error_class([u'Please enter the course prefix in the following format: CSCI-UA'])
		return cleaned_data



class CourseModelForm(forms.ModelForm):
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	prof_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	course_prefix = forms.CharField(max_length=128, help_text="Enter Course Prefix: ")
	course_number = forms.CharField(max_length=128, help_text="Enter Course Number: ")
	professor    = forms.CharField(max_length=128, help_text="Enter Professor's Full Name: ")
	course_name   = forms.CharField(max_length=128, help_text="Enter Course's Name: ")

	# How should I go about adding category into the form?

	class Meta:
		model = CourseModel 
		exclude = ('course_user',)

class StudentCourseModelForm(forms.ModelForm):
	coursegrade  = forms.ChoiceField(help_text="Enter Grade Received: ", choices = GRADE_CHOICES)
	class Meta:
		model = StudentCourseModel 
		exclude = ('course_user', 'course_model', 'verified')

class SearchForm(forms.Form):
	course_prefix = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Course Prefix'}))
	course_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Course Number'}))
	course_name   = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Course Name'}))
	professor    = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Professor Name'}))







