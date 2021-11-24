from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Hotel_User
from .models import Tasks

# Create your views here.
def users(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Hotel_User.objects.filter(user_email=user_email)[0]
            tasks = Tasks.objects.filter(username=request.user)
        except:
            return redirect('../admin')
        return render(request, "users.html", {'user':user,'tasks':tasks})
    else:
        messages.info(request,'Please login to access your Dashboard !')
        return redirect('login')

def accomplish(request):
    pass