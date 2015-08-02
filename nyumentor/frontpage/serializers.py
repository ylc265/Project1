from rest_framework import serializers
from frontpage.models import StudentCourseModel
__author__ = 'ylc265'

class StudentCourseModelSerializer(serializers.ModelSerializer):
    # !!! slug related field
    class Meta:
        model = StudentCourseModel
        fields = ('id', 'course_user', 'course_model',
                  'semester', 'year', 'pub_date')
