from django.core.checks import messages
from django.shortcuts import render
from .models import Queries
from django.contrib import messages
# Create your views here.

def home(request):
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
    return render(request,'contact.html')