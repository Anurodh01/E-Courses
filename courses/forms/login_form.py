from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError



class LoginForm(AuthenticationForm):
    pass
    # email= forms.EmailField(max_length=40, required=True)
    
    # username= forms.EmailField(max_length=30, required=True, label='Email Address: ')


    # def clean(self):       
    #     email= self.cleaned_data['username']
    #     password= self.cleaned_data['password']
    #     try:
    #         user= User.objects.get(email= email)
    #         if(user is None):
    #             raise ValidationError("Email or password is invalid.")
    #         result= authenticate(username= user.username, password= password)
    #         if result is not None:
    #             login(self.request, result)
    #         else:
    #             raise ValidationError("Email or password is invalid.")
    #     except:
    #         raise ValidationError("Email or Password is invalid.")