from courses.models import Course, Prerequisite, Tag, Learning
# from courses.models import Video
# from courses.models import UserCourse
# from courses.models import Payment
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'
    
