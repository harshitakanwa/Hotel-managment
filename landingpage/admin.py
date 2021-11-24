from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Queries

# Register your models here.
admin.site.register(Queries)
admin.site.unregister(Group)
admin.site.site_header = "Hotel Transylvenia Administration"