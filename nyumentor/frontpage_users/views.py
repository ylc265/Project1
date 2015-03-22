from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from frontpage.forms import CourseForm
from frontpage.models import CourseModel, StudentCourseModel
from frontpage_users.forms import UserForm, UserProfileForm 
from frontpage_users.models import UserProfile
from frontpage.views import index

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
def register(request):

	registered = False 

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user 

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
			return index(request)

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
			'frontpage_users/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			# if there's a user object 
			if user.is_active:
				# user might not be active
				login(request, user) # log into session
				return HttpResponseRedirect('/frontpage/')
			else:
				return HttpResponse("Your account is disabled")

		else:
			print("Invalid login details:{0}, {1}".format(username, password))
			return HttpResponse("Invalid Login details.")

	else:
		return render(request, 'frontpage_users/login.html', {})

def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/frontpage/')
