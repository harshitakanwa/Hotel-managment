from django.core.checks import messages
from django.shortcuts import render,redirect
from .models import Queries
from django.contrib import messages
from accounts.models import Hotel_User
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            library_user = Hotel_User.objects.filter(user_email=user_email)[0]
        except:
            return render(request,'home.html')
        return render(request, "home.html", {'library_user':library_user})
    else:
        return render(request,'home.html')

def contact(request):
    if request.method=='POST':
        email = request.POST['email']
        query = request.POST['query']
        Query = Queries(
            email = email,
            query = query
        )
        Query.save()
        messages.info(request,'We have got your query/suggestion. We will get back to you soon!')
    if request.user.is_authenticated:
        return redirect('users')
    else:
        return render(request,'contact.html')



# Error Pages Handling

def error_404(request):
        return render(request, 'error_404.html', {})

def error_500(request):
        return render(request, 'error_500.html', {})

def error_403(request):
        return render(request, 'error_403.html', {})

def error_400(request):
        return render(request, 'error_400.html', {})