from django.shortcuts import render, HttpResponse
from courses.models import Course,UserCourse
from courses.models import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def home(request):
    allcourses = Course.objects.filter(active= True)
    if request.user.is_authenticated:
        user= request.user
        usercourses = UserCourse.objects.filter(user= user).order_by('-date')
        
    context={'courses':allcourses}
    return render(request, 'courses/index.html', context)

@api_view(['GET'])
def getCourseList(request):
    allcourses = Course.objects.filter(active= True)
    serializer= CourseSerializer(allcourses, many = True)
    return Response(serializer.data)