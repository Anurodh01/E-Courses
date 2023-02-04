from django.shortcuts import render, HttpResponse, redirect
from courses.models import Course, Video, UserCourse
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/login'),name='dispatch')
class MycourseView(ListView):
    template_name= 'courses/mycourses.html'
    context_object_name= 'courses'
    def get_queryset(self):
        usercourse= UserCourse.objects.filter(user= self.request.user)
        l= []
        for i in usercourse:
            if i.course.active== True:
                l.append(i)
        return l
    
