from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# This is a home page where Hello django msg will appear
def home(request):
    return HttpResponse("Hello, Django!!!")