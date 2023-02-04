from django import template
import math
from courses.models import UserCourse
register= template.Library()


@register.simple_tag
def cal_sell_price(price , discount):
    if(discount is None or discount is 0):
        return price
    sellprice = price - (price * discount * 0.01)  
    return math.floor(sellprice)

@register.filter
def rupee(price):
    return f'₹{price}'

@register.filter
def capitalize(string):
    return string.title()

@register.simple_tag
def is_enrolled(request , course):
    user= request.user
    try:
        usercourse= UserCourse.objects.get(user= user, course= course)
        return True
    except:
        return False
