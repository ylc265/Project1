from frontpage.models import StudentCourseModel
from rest_framework import serializers
from django.contrib.auth.models import User
__author__ = 'ylc265'

class UserSerializer(serializers.ModelSerializer):
    # scm = serializers.PrimaryKeyRelatedField(many=True, queryset=StudentCourseModel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')