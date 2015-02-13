from django.contrib import admin
from frontpage.models import Category, CourseModel
# Register your models here.
# 
class CourseModelAdmin(admin.ModelAdmin):
	list_display = ('coursenumber', 'professor', 'coursename')
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CourseModel, CourseModelAdmin)
# admin.site.register(CourseName)
# admin.site.register(CourseNumber)
# admin.site.register(Professor)
