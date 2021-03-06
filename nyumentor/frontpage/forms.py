import re
from django import forms 
from django.utils.translation import ugettext_lazy as _ 
from haystack.forms import SearchForm
from frontpage.models import StudentCourseModel, CourseModel 

course_number_pattern = re.compile(r'\w+-\w+ \d+', re.IGNORECASE)
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
SEMESTER = (
		('Spring', 'Spring'),
		('Summer', 'Summer'),
		('Fall', 'Fall'),
		('Winter', 'Winter'),
	)

class CourseForm(forms.Form):
	'''
	This is the form I am going to use to create both the CourseModel and the 
	StudentCourseModel
	'''
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	prof_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	# course_prefix = forms.CharField(max_length=128, help_text="Enter Course Prefix: ")
	course_number = forms.CharField(max_length=128, help_text="Enter Course Number: ")
	professor    = forms.CharField(max_length=128, help_text="Enter Professor's Full Name: ")
	course_name   = forms.CharField(max_length=128, help_text="Enter Course's Name: ")
	course_grade  = forms.ChoiceField(help_text="Enter Grade Received: ", choices = GRADE_CHOICES)
	semester  = forms.ChoiceField(help_text="Enter Semester Taken: ", choices = SEMESTER)
	year = forms.IntegerField(help_text="Enter Year Taken: ", min_value=1900, max_value=2200)
	# !!! In the future, maybe regular expression for the input. For example, CS_UA, must always
	# follow a standard.
	def clean(self):
		cleaned_data = super(CourseForm, self).clean()
		course_number_valid = cleaned_data.get('course_number')
		if not course_number_pattern.match(course_number_valid):
			self._errors['course_number'] = self.error_class([u'Please enter the course number in the format seen on Albert. Example: CSCI-UA 102'])
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

# class SearchForm(forms.Form):
# 	# course_prefix = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-box',
# 	# 																			  'placeholder': 'Course Prefix',
# 	# 																			  'size': 15,}))
# 	course_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input typeahead',
# 																				  'autocomplete': 'off',
# 																				  'placeholder': 'Course Number',
# 																				  'size': 15,}))
# 	# course_name   = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-box',
# 	# 																			  'placeholder': 'Course Name',
# 	# 																			  'size': 15,}))
# 	professor    = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input typeahead',
# 																				 'autocomplete': 'off',
# 																				  'placeholder': 'Professor Name',
# 																				  'size': 15,}))
# 	def clean(self):
# 		cleaned_data = super(SearchForm, self).clean()
# 		if cleaned_data['course_number'] == '' and cleaned_data['professor'] == '':
# 			self._errors['course_number'] = self.error_class([u'Please enter something'])
# 		return cleaned_data

class StyledSearchForm(SearchForm):
	q = forms.CharField(required=False, label=_('Search'), widget=forms.TextInput(attrs={'class': 'form-input typeahead',
																				  'autocomplete': 'off',
																				  'placeholder': 'Course Number',
																				  'size': 15,}))

