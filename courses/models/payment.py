from django.db import models
from courses.models import Course, UserCourse
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField(max_length=100, null= False)
    payment_id = models.CharField(max_length=100, null= True)
    user_course= models.ForeignKey(UserCourse, on_delete=models.CASCADE, null= True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null= False)
    course= models.ForeignKey(Course, on_delete=models.CASCADE, null= False)
    date= models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}- {self.course}- {self.status}'