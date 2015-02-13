from django.shortcuts import render
from frontpage.models import CourseModel
# Create your views here.


def index(request):
	# Just list all the courses ordered by course number
	course_list = CourseModel.objects.order_by('coursenumber')
	context_dict = {'courses': course_list}

	return render(request, 'frontpage/index.html', context_dict)

def get_cpage(request, course_slug):
	context_dict = {}

	try:
		course = CourseModel.objects.get(slug=course_slug)
		# context_dict['course_name'] = course.coursename
		# context_dict['course_number'] = course.coursenumber 
		# context_dict['professor'] = course.professor
		context_dict['course'] = course

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
