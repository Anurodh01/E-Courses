from django.shortcuts import render, HttpResponse, redirect
from courses.models import Course, Video, Payment , UserCourse
from django.contrib import messages
from courseselling.settings import SECRET_KEY, KEY_ID
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import razorpay
client = razorpay.Client(auth=(KEY_ID, SECRET_KEY))


@login_required(login_url='/login')
def checkout(request, slug):
    payment= None
    course= Course.objects.filter(slug=slug).first()
    user= request.user
    action= request.GET.get('action')    #if this action is there then only create the order id
    if action is not None:
        usercourse= UserCourse.objects.filter(user= user, course= course).first()
        if usercourse is not None:
            messages.warning(request, "You have already paid for this course.!!")
            return redirect(f'/checkout/{course.slug}')
        amount= int(course.price- (course.price* course.discount * 0.01))*100
        data={
            "amount": 100,
            "currency": "INR",
            "receipt": f'E-learning_{int(time())}',
            "notes": {'name': f'{user.first_name} { user.last_name }','email': user.email}
        }
        order= payment = client.order.create(data=data)
        payment= Payment()
        payment.order_id= order.get('id')
        payment.user= user
        payment.course= course
        payment.save()
        context={'course':course, 'order': order,'payment': payment}
        return render(request,'courses/checkout.html', context)            
    context={'course':course}
    return render(request,'courses/checkout.html', context)


@csrf_exempt
def verify_payment(request):
    if request.method=="POST":
        data= request.POST
        client.utility.verify_payment_signature(data)
        razorpay_order_id = data.get('razorpay_order_id') 
        razorpay_payment_id = data.get('razorpay_payment_id')

        paymentobj = Payment.objects.get(order_id= razorpay_order_id)
        usercourseobj= UserCourse()
        usercourseobj.user= paymentobj.user
        usercourseobj.course= paymentobj.course
        usercourseobj.save()
        paymentobj.payment_id= razorpay_payment_id
        paymentobj.user_course= usercourseobj
        paymentobj.status= True
        paymentobj.save()
        messages.success(request, "Your payment is Successful.")
        return redirect('mycourses')


