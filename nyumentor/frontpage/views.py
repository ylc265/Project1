from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.defaultfilters import slugify
from frontpage.context_processors import main_proc
from frontpage.models import CourseModel, StudentCourseModel
from frontpage.forms import CourseForm, CourseModelForm, SearchForm
from frontpage_users.forms import MyAuthenticationForm
from frontpage_users.models import UserProfile
# Create your views here.


def index(request):
	authentication_form = MyAuthenticationForm
	course_list = StudentCourseModel.objects.all()
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			# This is the preliminary way of searching, later on I will have to refine this
			cnumber = form.cleaned_data.get('course_number')
			professor = form.cleaned_data.get('professor')
			# slug = '{}-{}-{}-{}'.format(slugify(cprefix), slugify(cnumber), slugify(cname), slugify(professor))
			if cnumber!='' and professor !='':
				course_model = CourseModel.objects.filter(course_number=cnumber, professor=professor)
			elif cnumber !='':
				course_model = CourseModel.objects.filter(course_number=cnumber)
			elif professor !='':
				course_model = CourseModel.objects.filter(professor=professor)
			course_list = StudentCourseModel.objects.filter(course_model=course_model)
	# Just list all the courses ordered by course number
	form = SearchForm()
	login_form = authentication_form(request)
	context_dict = {'courses': course_list,
					'form': form,
					'login_form': login_form}

	# return render(request, 'frontpage/index.html', context_dict)
	return render(request, 'base.html', {'courses':course_list,},
		context_instance=RequestContext(request, [main_proc]))




def get_cpage(request, course_slug):
	context_dict = {}

	try:
		course = CourseModel.objects.get(slug=course_slug)
		s_courses = StudentCourseModel.objects.filter(course_model = course)
		# context_dict['course_name'] = course.coursename
		# context_dict['course_number'] = course.coursenumber 
		# context_dict['professor'] = course.professor
		context_dict['courses'] = s_courses
	except CourseModel.DoesNotExist:
		pass
	
	return render(request, 'frontpage/courseinfo.html', context_dict)

def get_prof(request, prof_slug):
	context_dict = {}

	try:
		courses = CourseModel.objects.filter(prof_slug = prof_slug)
		print(courses)
		context_dict['courses'] = courses 
	except CourseModel.DoesNotExist:
		pass
	return render(request, 'frontpage/profinfo.html', context_dict)
	'''
	prof_list = CourseModel.objects.values('professor').distinct()
	context_dict = {'professors': prof_list}

	return render(request, 'frontpage/professors.html', context_dict)
	'''

def add_course(request):
	''' add CourseModel and link user to the course '''
	if request.user.is_authenticated():
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
					course_prefix = course_prefix,
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



				'''
				form_object = form.save(commit=False)
				user = UserProfile.objects.get(user = request.user)
				form_object.course_user = user
				form_object.save()
				'''
				# return index(request)
				return HttpResponseRedirect('/frontpage/')
			else:
				print(form.errors) 
		else:
			form = CourseForm()

		return render(request, 'frontpage/add_course.html', {'form': form})
	else:
		return index(request)

