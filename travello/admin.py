from django.contrib import admin
from .models import Cities,Hotel,Room_Type,Room_History

# Register your models here.
admin.site.register(Cities)
admin.site.register(Hotel)
admin.site.register(Room_Type)
admin.site.register(Room_History)