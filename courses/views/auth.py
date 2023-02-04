from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationFrom, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login , logout
# Create your views here.

class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form= RegistrationFrom()
        return render(request, 'courses/signup.html', context={'form':form})
    
    def post(self, request):
        form = RegistrationFrom(request.POST)
        if(form.is_valid()):
            user= form.save()
            return redirect('login')
        return render(request, 'courses/signup.html', context={'form': form})

        


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form= LoginForm()
        context={'form':form}
        return render(request, 'courses/login.html', context=context)

    def post(self, request):
        next_page= request.GET.get('next')
        form = LoginForm(request= request, data= request.POST)
        if(form.is_valid()):
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(request, username= username, password= password )
            if(user is not None and next_page is not None):
                login(request, user)
                return redirect(next_page)
            elif user is not None and next_page is None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'coureses/login.html', context={'form': form})
        return render(request, 'courses/login.html', context={'form': form})
    
def logoutpage(request):
    logout(request)
    return redirect('home')