from django import forms 
from frontpage.models import Category, CourseModel 

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

class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ('name',)

class CourseModelForm(forms.ModelForm):
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	prof_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	coursenumber = forms.CharField(max_length=128, help_text="Enter Course Number: ")
	professor    = forms.CharField(max_length=128, help_text="Enter Professor's Full Name: ")
	coursename   = forms.CharField(max_length=128, help_text="Enter Course's Name: ")
	coursegrade  = forms.ChoiceField(help_text="Enter Grade Received: ", choices = GRADE_CHOICES)
	# How should I go about adding category into the form?

	class Meta:
		model = CourseModel 
		exclude = ()