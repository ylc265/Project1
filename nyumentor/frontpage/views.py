from django.shortcuts import render
from django.template.defaultfilters import slugify
from frontpage.models import CourseModel
from frontpage.forms import CategoryForm, CourseModelForm, SearchForm
from frontpage_users.models import UserProfile
# Create your views here.


def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			cnumber = form.cleaned_data.get('coursenumber')
			professor = form.cleaned_data.get('professor')
			slug = '{}-{}'.format(slugify(cnumber), slugify(professor))
			return get_cpage(request, slug)
	# Just list all the courses ordered by course number
	course_list = CourseModel.objects.order_by('coursenumber')
	form = SearchForm()
	context_dict = {'courses': course_list,
					'form': form}

	return render(request, 'frontpage/index.html', context_dict)

def get_cpage(request, course_slug):
	context_dict = {}

	try:
		courses = CourseModel.objects.filter(slug=course_slug)
		# context_dict['course_name'] = course.coursename
		# context_dict['course_number'] = course.coursenumber 
		# context_dict['professor'] = course.professor
		context_dict['courses'] = courses

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
			form = CourseModelForm(request.POST)

			if form.is_valid():
				form_object = form.save(commit=False)
				user = UserProfile.objects.get(user = request.user)
				form_object.course_user = user
				form_object.save()
				return index(request)
			else:
				print(form.errors) 
		else:
			form = CourseModelForm()

		return render(request, 'frontpage/add_course.html', {'form': form})
	else:
		return index(request)
