from django.contrib import admin
from frontpage.models import Category, CourseModel
from frontpage_users.models import UserProfile
# Register your models here.
# 
class CourseModelAdmin(admin.ModelAdmin):
	list_display = ('coursenumber', 'professor', 'coursename', 'course_user')

	

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'get_courses')

	def get_courses(self, obj):
		return '\n'.join([str(course) for course in obj.coursemodel_set.all()])

admin.site.register(Category, CategoryAdmin)
admin.site.register(CourseModel, CourseModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(CourseName)
# admin.site.register(CourseNumber)
# admin.site.register(Professor)
