import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nyumentor.settings')

import django
django.setup()

from frontpage.models import CourseModel, Category

def populate():
	help_populate('MAP', 'Whatever', 'MAP_UA 101', 'Bullshit', 'A')
	help_populate('MATH', 'Cheegar', 'MATH_UA 121', 'Calculus I', 'B')
	help_populate('MATH', 'Seline', 'MATH_UA 122', 'Calculus II', 'C')
	help_populate('MATH', 'Bertow', 'MATH_UA 123', 'Calculus III', 'D')

	help_populate('ENG', 'Stein', 'ENG_UA 121', 'English I', 'A-')
	help_populate('ENG', 'Seline', 'ENG_UA 122', 'English II', 'B+')
	help_populate('ENG', 'Seline', 'ENG_UA 123', 'English III', 'A')

	help_populate('CS', 'Davis', 'CS_UA 121', 'DS', 'A')
	help_populate('CS', 'Siegel', 'CS_UA 121', 'Algo', 'B')
	help_populate('CS', 'Bernstein', 'CS_UA 123', 'Algo', 'C')
	help_populate('CS', 'Davis', 'CS_UA 121', 'DS', 'B')

def help_populate(catname, profname, cnumname, cnamename, coursegrade):
	cat = add_cat(catname)
	add_course(cat = cat, cnum = cnumname,
		prof = profname, cname = cnamename, cgrade = coursegrade)

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c 

def add_course(cat, cnum, prof, cname, cgrade):
	ac = CourseModel.objects.get_or_create(category = cat, coursenumber = cnum,
		professor = prof, coursename = cname, coursegrade = cgrade)[0]
	
	ac.save()
	return ac
'''
def add_cnum(name):
	c = CourseNumber.objects.get_or_create(name=name)[0]
	return c 

def add_cname(name):
	c = CourseName.objects.get_or_create(name=name)[0]
	return c 

def add_prof(name):
	c = Professor.objects.get_or_create(name=name)[0]
	return c 

def add_course(cat, cnum, prof, cname):
	ac = CourseModel.objects.get_or_create(category = cat)[0]
	ac.save()
	ac.coursenumber.add(cnum)
	ac.professor.add(prof)
	ac.coursename.add(cname)
	return ac
'''
if __name__ == '__main__':
	print("Starting Rango population script ...")
	populate()