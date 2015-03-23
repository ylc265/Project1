from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from frontpage.forms import CourseForm
from frontpage.models import CourseModel, StudentCourseModel
from frontpage_users.forms import UserForm, UserProfileForm 
from frontpage_users.models import UserProfile

def user_profile(request):
	context_dict = {}
	if request.user.is_authenticated():
		profile = UserProfile.objects.get(user=request.user)
		course_list = profile.studentcoursemodel_set.all()
		context_dict['profile'] = profile
		context_dict['course_list'] = course_list
		if request.method == 'POST':
			form = CourseForm(request.POST)
			if form.is_valid():
				course_number = form.cleaned_data['course_number']
				professor     = form.cleaned_data['professor']
				course_name   = form.cleaned_data['course_name']
				course_grade  = form.cleaned_data['course_grade']
				semester      = form.cleaned_data['semester']
				year          = form.cleaned_data['year']

				course_model = CourseModel.objects.get_or_create(
					course_number = course_number,
					professor = professor,
					course_name = course_name)[0]
				# print(course_model)
				# print(type(course_model))
				course_user = UserProfile.objects.get(user = request.user)
				StudentCourseModel.objects.get_or_create(
					course_user = course_user,
					course_model = course_model,
					course_grade = course_grade,
					semester = semester,
					year = year)
			else:
				print(form.errors) 
		else:
			context_dict['course_form'] = CourseForm()
	return render(request,
		'frontpage_users/user_profile.html',
		context_dict
	)

