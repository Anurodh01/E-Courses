from django.shortcuts import render, HttpResponse, redirect
from courses.models import Course, Video, UserCourse
from django.contrib import messages


def coursepage(request, slug):
    serial_number= request.GET.get('lecture')
    nextlecture = None
    previouslecture= None
    if serial_number is None:
        serial_number= 1
        nextlecture= 1
        previouslecture= None
    else:
        nextlecture= int(serial_number)
        previouslecture= int(serial_number)     
    course= Course.objects.filter(slug=slug).first()
    video= Video.objects.filter(course=course, serial_no= serial_number).first()
    total_videos= course.video_set.all()
    if previouslecture is not None:
        previouslecture  -= 1
        if previouslecture == 0:
            previouslecture = None 
    if len(total_videos) <= nextlecture:
        nextlecture= None
    else:
        nextlecture += 1
    if((request.user.is_authenticated is False) and (video.is_preview is False)):
        messages.warning(request,"Please login to continue.")
        return redirect('login')
    if (request.user.is_authenticated is True ) and (video.is_preview is False):
        user= request.user
        try:
            usercourse= UserCourse.objects.get(user= user, course= course)
        except:
            messages.info(request, "You are not enrolled in this course yet!!! ENROLL NOW....");
            return redirect(f'/checkout/{slug}')
    context={'course':course, 'video':video, 'nextlecture':nextlecture, 'previouslecture':previouslecture}
    return render(request,'courses/coursepage.html', context)
