from django.db import models

# Create your models here.
class Hotel_User(models.Model):
    user_first_name = models.CharField(max_length = 100)
    user_last_name = models.CharField(max_length = 100, default=None)
    user_phone = models.BigIntegerField()
    user_password = models.TextField()
    user_aadhaar = models.BigIntegerField()
    user_address = models.TextField()
    user_dob = models.DateField()
    user_email = models.TextField()
    user_gender = models.CharField(max_length = 6)
    user_status =models.CharField(max_length=20, default='new')
    user_joined_date = models.DateField()
    user_photo  = models.ImageField(upload_to = 'user_photos',default='photo')
    user_aadhar_photo  = models.ImageField(upload_to = 'user_aadhaar_photo',default='photo')

def __str__(self):
    return self.user.user_first_name
