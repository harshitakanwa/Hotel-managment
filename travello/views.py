from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, UserManager
from accounts.models import Hotel_User
from .models import Cities, Hotel, Room_History, Room_Type
import datetime
from . import required_functions
import pandas as pd
import threading

# Create your views here.
def explore(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Hotel_User.objects.filter(user_email=user_email)[0]
            cities = Cities.objects.all()
        except:
            return redirect('../admin')
        return render(request, "explore.html", {'user':user,'cities':cities})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def hotel_view(request, *args, **kwargs):
    hotel_id = int(kwargs['id'])
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Hotel_User.objects.filter(user_email=user_email)[0]
            city = Cities.objects.filter(id=hotel_id)[0]
            room_type = Room_Type.objects.filter(room_city=city)
            hotel_rooms = Hotel.objects.filter(id=-1)
            for room in room_type:
                hotel_rooms |= Hotel.objects.filter(room=room)
        except:
            return redirect('../admin')
        return render(request, "hotel.html", {'user':user,'hotel_rooms':hotel_rooms,'city':city})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def catalogue(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Hotel_User.objects.filter(user_email=user_email)[0]
            books = Book.objects.all()
        except:
            return redirect('../admin')
        return render(request, "catalogue.html", {'user':user,'books':books})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def room_view(request, *args, **kwargs):
    hotel_id = int(kwargs['id'])
    room_id = int(kwargs['room_id'])
    username = str(request.user)
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=username).values()[0].get('email')
        try:
            user = Hotel_User.objects.filter(user_email=user_email)[0]
            city = Cities.objects.filter(id=hotel_id)[0]
            room_type = Room_Type.objects.filter(room_city=city,id=room_id)[0]
            hotel_room = Hotel.objects.filter(room=room_type)[0]
        except:
            return redirect('../../../admin')
        return render(request, "room.html", {'user':user,'hotel_room':hotel_room,'city':city})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def dates(start_date, today, end_date):
    L = []
    if start_date<today:
        start_date=today
    i=0
    while start_date<end_date:
        L.append(today + datetime.timedelta(days=i))
        start_date +=  datetime.timedelta(days=1)
        i+=1
    return set(L)



def book_room(request,*args,**kwargs):
    hotel_id = int(kwargs['id'])
    room_id = int(kwargs['room_id'])
    username = str(request.user)
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=username).values()[0].get('email')
        try:
            user = Hotel_User.objects.filter(user_email=user_email)[0]
            city = Cities.objects.filter(id=hotel_id)[0]
            room_type = Room_Type.objects.filter(room_city=city,id=room_id)[0]
            hotel_room = Hotel.objects.filter(room=room_type)[0]
            today_date = datetime.date.today()
            active_history = Room_History.objects.filter(room_id=room_id,room_leaving_date__gte=today_date).values()
            booked_dates = set()
            for history in active_history:
                all_dates = set(pd.date_range(start=history.get('room_taking_date'),end=history.get('room_leaving_date')).strftime("%Y-%m-%d"))
                booked_dates = set.union(booked_dates,all_dates)
            booked_dates = list(booked_dates)
            #booked_dates = json.dumps(booked_dates)
            print(booked_dates)
        except:
            return redirect('/admin')
        return render(request, "book_room.html", {'user':user,'hotel_room':hotel_room,'city':city,'booked_dates':booked_dates})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')
    

def checkout(request,*args,**kwargs):
    if request.method=='POST':
        room_taking_date = request.POST['room_taking_date']
        room_leaving_date = request.POST['room_leaving_date']
        try:
            hall_price = request.POST['hall_price']
        except:
            hall_price = 0
        try:
            meal_price = request.POST['meal_price']
        except:
            meal_price = 0
        try:
            gym_price = request.POST['gym_price']
        except:
            gym_price = 0
        try:
            room_price = request.POST['room_price']
        except:
            room_price = 0
        total_price = int(hall_price) + int(meal_price) + int(gym_price) + int(room_price)
        today_date = datetime.date.today()
    return render(request,'checkout.html',{'total_price':total_price,'today_date':today_date,'room_leaving_date':room_leaving_date,'room_taking_date':room_taking_date,'hall_price':hall_price,'meal_price':meal_price,'gym_price':gym_price,'room_price':room_price})


def save_data(request, **kwargs):
    print(kwargs)
    city_id = kwargs['id']
    room_id = kwargs['room_id']
    d = datetime.datetime.strptime("11/24/1995", '%m/%d/%Y').date()
    room_user = str(request.user)
    hotel_user = User.objects.filter(username=room_user).values()[0]
    user_email = hotel_user.get('email')
    user_first_name = hotel_user.get('first_name')
    room_id = room_id
    room_taking_date = datetime.datetime.strptime(request.POST['room_taking_date'], '%m/%d/%Y').date()
    room_leaving_date = datetime.datetime.strptime(request.POST['room_leaving_date'], '%m/%d/%Y').date()
    room_booking_date = datetime.date.today()
    print(request.POST)
    room_price = request.POST['room_price']
    hall_price = request.POST['hall_price']
    meal_price = request.POST['meal_price']
    gym_price = request.POST['gym_price']
    total_price = request.POST['total_price']

    history = Room_History(
        room_user = room_user,
        room_id = room_id,
        room_taking_date = room_taking_date,
        room_leaving_date = room_leaving_date,
        room_booking_date = room_booking_date,
        total_bill = total_price
    )
    history.save()
    email_context = {
        'room_user' : room_user,
        'room_id' : room_id,
        'room_taking_date' : room_taking_date,
        'room_leaving_date' : room_leaving_date,
        'room_booking_date' : room_booking_date,
        'room_price' : room_price,
        'hall_price' : hall_price,
        'meal_price' : meal_price,
        'gym_price' : gym_price,
        'total_price' : total_price
    }
    email_thread = threading.Thread(target=required_functions.send_room_details,args=(user_email,room_user,user_first_name,email_context))
    email_thread.start()
    messages.info(request,'Your booking is Successful. Please check your email for complete details !')
    return redirect(f'/hotels/{city_id}/{room_id}')

def return_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                user_email = User.objects.filter(username=request.user).values()[0].get('email')
                try:
                    user = Hotel_User.objects.filter(user_email=user_email).values()[0]
                    book = Book.objects.filter(id=book_id).values()[0]
                    taken = False
                    username=str(request.user)
                    taken=False
                    if book.get('book_owner')==username:
                        owned = True
                    else:
                        owned = False
                    if book.get('book_sale')==True:
                        for_sale = True
                    else:
                        for_sale = False
                    print('owned',owned)
                    print(book_id)
                    book_history = BookHistory.objects.all()
                    print(book_history)
                    book_history = BookHistory.objects.filter(book_id=book_id,book_returndate=datetime.datetime(1111,11,11).date(),book_currentholder=username)
                    print(book_history)
                    book_history.update(book_returndate=datetime.date.today())
                    for history in book_history:
                        history.save()
                    rating = book.get('book_rating')*[0]
                    print(rating)
                    Book.objects.filter(id=book_id).update(book_currentholder='Admin')
                    for book in Book.objects.filter(id=book_id):
                        book.save()
                except:
                    return redirect('../../../admin')
                return redirect('book_view',book_id) #render(request, "book.html", {'user':user,'book':book,'rating':rating,'taken':taken,'owned':owned,'for_sale':for_sale})
            else:
                messages.info(request, 'Please login to access the book catalogue !')
                return redirect('login')
        else:
            return 0

def sell_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                user_email = User.objects.filter(username=request.user).values()[0].get('email')
                try:
                    user = Hotel_User.objects.filter(user_email=user_email).values()[0]
                    book = Book.objects.filter(id=book_id).values()[0]
                    taken = False
                    username=str(request.user)
                    if book.get('book_currentholder')=='Admin':
                        taken=False
                    else:
                        taken=True
                    if book.get('book_owner')==username:
                        owned = True
                    else:
                        owned = False

                    for_sale = True

                    print('owned',owned)
                    #book_history = BookHistory.objects.filter(id=book_id,book_returndate=datetime.datetime(1111,11,11).date(),book_currentholder=username)
                    #book_history.update(book_returndate=datetime.date.today())
                    #for history in book_history:
                    #    history.save()
                    rating = book.get('book_rating')*[0]
                    print(rating)
                    Book.objects.filter(id=book_id).update(book_sale=True)
                    for book in Book.objects.filter(id=book_id):
                        book.save()
                except:
                    return redirect('../../../admin')
                return redirect('book_view',book_id) #render(request, "book.html", {'user':user,'book':book,'rating':rating,'taken':taken,'owned':owned,'for_sale':for_sale})
            else:
                messages.info(request, 'Please login to access the book catalogue !')
                return redirect('login')
        else:
            return 0

def buy_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                user_email = User.objects.filter(username=request.user).values()[0].get('email')
                try:
                    user = Hotel_User.objects.filter(user_email=user_email).values()[0]
                    book = Book.objects.filter(id=book_id).values()[0]
                    taken = False
                    username=str(request.user)
                    if book.get('book_currentholder')=='Admin':
                        taken=False
                    else:
                        taken=True
                    if book.get('book_owner')==username:
                        owned = True
                    else:
                        owned = False
                    print('owned',owned)
                    #book_history = BookHistory.objects.filter(id=book_id,book_returndate=datetime.datetime(1111,11,11).date(),book_currentholder=username)
                    #book_history.update(book_returndate=datetime.date.today())
                    #for history in book_history:
                    #    history.save()
                    rating = book.get('book_rating')*[0]
                    print(rating)
                    Book.objects.filter(id=book_id).update(book_sale=False)
                    Book.objects.filter(id=book_id).update(book_owner=username)
                    for book in Book.objects.filter(id=book_id):
                        book.save()
                    for_sale = False
                except:
                    return redirect('../../../admin')
                return redirect('book_view',book_id) #render(request, "book.html", {'user':user,'book':book,'rating':rating,'taken':taken,'owned':owned,'for_sale':for_sale})
            else:
                messages.info(request, 'Please login to access the book catalogue !')
                return redirect('login')
        else:
            return 0

def request_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                try:
                    book = Book.objects.filter(id=book_id).values()[0]
                    username=str(request.user)
                    book_request  = Request(
                        requested_user = book.get('book_currentholder'),
                        requested_book = book_id,
                        requesting_user = username
                    )
                    book_request.save()
                except:
                    return redirect('/admin')
                return redirect('.') #render(request, "book.html", {'user':user,'book':book,'rating':rating,'taken':taken,'owned':owned,'for_sale':for_sale})
            else:
                messages.info(request, 'Please login to access the book catalogue !')
                return redirect('login')
        else:
            return 0