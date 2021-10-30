from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def users(request):
    if request.user.is_authenticated:
        return render(request,'users.html')
    else:
        messages.info(request,'Please login to access your Dashboard !')
        return redirect('login')