
from django.contrib import admin
from frontpage.models import StudentCourseModel, CourseModel
from frontpage_users.models import UserProfile
# Register your models here.
# 

class CourseModelAdmin(admin.ModelAdmin):
	list_display = ('course_prefix', 'course_number', 'course_name', 'professor')
	prepopulated_fields = {'slug':('course_prefix', 'course_number', 'professor'),
						   'prof_slug': ('professor',)}

	

class StudentCourseModelAdmin(admin.ModelAdmin):
	list_display = ('course_model', 'course_grade', 'course_user')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'get_courses')

	def get_courses(self, obj):
		return '\n'.join([str(course) for course in obj.studentcoursemodel_set.all()])

admin.site.register(StudentCourseModel, StudentCourseModelAdmin)
admin.site.register(CourseModel, CourseModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(CourseName)
# admin.site.register(CourseNumber)
# admin.site.register(Professor)
