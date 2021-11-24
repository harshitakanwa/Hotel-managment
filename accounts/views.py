import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import Hotel_User
import datetime
from . import required_functions
import threading
# Create your views here.



def login(request):
    if request.user.is_authenticated:
        return redirect('users')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['user_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("users")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):

    new_id = User.objects.order_by('id').last().id+1
    year = str(datetime.date.today().year%100)
    username = f'{year}HTU{new_id:0004}'
    if request.method == 'POST':
        user_first_name = request.POST['user_first_name']
        user_last_name = request.POST['user_last_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_phone = request.POST['user_phone']
        user_aadhaar = request.POST['user_aadhaar']
        user_dob = request.POST['user_dob']
        user_address = request.POST['user_address']
        user_gender = request.POST['user_gender']
        user_joined_date = datetime.date.today()
        user_photo = request.FILES['user_photo']
        user_aadhar_photo = request.FILES['user_aadhar_photo']
        user_password1 = request.POST['user_password1']

    
        if not required_functions.validate(request,user_password, user_password1, user_aadhaar, user_email,user_phone):
            return redirect('register')
        else:
            user1 = Hotel_User(
                user_first_name = user_first_name,
                user_last_name = user_last_name,
                user_phone = user_phone,
                user_email = user_email,
                user_password = user_password,
                user_aadhaar = user_aadhaar,
                user_address = user_address,
                user_dob = user_dob,
                user_gender = user_gender,
                user_joined_date = user_joined_date,
                user_aadhar_photo = user_aadhar_photo,
                user_photo = user_photo
                )
            user1.save();
            user2 = User.objects.create_user(
                username=username,
                password=user_password,
                email=user_email,
                first_name=user_first_name,
                last_name=user_last_name
                )
            user2.save()
            
            thread = threading.Thread(target=required_functions.send_user_details, args=(user_email, username, user_password, user_first_name))
            thread.start()
            messages.info(request, 'Please check your email for Login Credentials !')
            return redirect('login')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def forgotPassword(request):
    if request.method == "POST":
        forgotEmail = request.POST['forgotEmail']
        if required_functions.validate_email(forgotEmail):
            if Hotel_User.objects.filter(user_email=forgotEmail).exists() or User.objects.filter(
                    email=forgotEmail).exists():
                userObjectnew = Hotel_User.objects.filter(user_email=forgotEmail).values()
                userObjectdef = User.objects.filter(email=forgotEmail).values()

                print('=======================>>>>>>',forgotEmail, userObjectdef[0].get('username'),
                      userObjectnew[0].get('user_password'),
                      userObjectnew[0].get('user_first_name'))

                thread = threading.Thread(target=required_functions.send_user_details,
                                          args=(forgotEmail, userObjectdef[0].get('username'),
                                                userObjectnew[0].get('user_password'),
                                                userObjectnew[0].get('user_first_name')))
                thread.start()
                messages.info(request, 'Please check your email for Login Credentials !')
                return redirect('login')

            else:
                messages.info(request, "OOPS, Looks Like you dont have an Account, Please Signup now !!")
                return redirect('forgotPassword')

        else:
            messages.info(request, 'Please Enter a valid Email !')
            return redirect('forgotPassword')

    else:
        return render(request, 'forgotpassword.html')