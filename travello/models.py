from django.db import models
import django.utils.timezone
#from django.db.models.base import Model

# Create your models here.
class Cities(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='city_images')
    rooms = models.PositiveIntegerField(default=0)
    description = models.TextField()
    address = models.TextField()
    def __str__(self):
         return self.name

class Hotel(models.Model):
    room = models.ForeignKey('Room_Type',on_delete=models.CASCADE)
    #room_type=models.CharField(max_length=30,choices=room_catchoice,default=1)
    room_description = models.TextField()

class Room_Type(models.Model):
    room_catchoice= [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
        ('Quad', 'Quad'),
        ('Queen','Queen'),
        ('King','King'),
        ('Twin','Twin'),
        ('Hollywood-Twin','Hollywood-Twin'),
        ('Studio','Studio'),
        ('Suite','Suite')
        ]
    room_image1 = models.ImageField(upload_to = 'room_images',default='room_images/room_image3.jpg')
    room_image2 = models.ImageField(upload_to = 'room_images',default='room_images/room_image1.jpg')
    room_image3 = models.ImageField(upload_to = 'room_images',default='room_images/room_image2.jpg')
    room_type = models.CharField(max_length=30,choices=room_catchoice,default='Single')
    room_price = models.PositiveIntegerField(default=300)
    room_city = models.ForeignKey('Cities',on_delete=models.CASCADE)
    room_rating = models.PositiveIntegerField(default=1)
    room_user = models.CharField(max_length=30, default='Admin')

class Room_History(models.Model):
    room_user = models.CharField(max_length=30, default='Admin')
    room_id = models.PositiveIntegerField()
    room_taking_date = models.DateField()
    room_leaving_date = models.DateField()
    room_booking_date = models.DateField(default=django.utils.timezone.now)
    total_bill = models.PositiveIntegerField(default=0)