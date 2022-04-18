from django.shortcuts import render
from django.http import HttpResponse 
import re
from django.shortcuts import render
from django.utils.timezone import datetime

# Create your views here.
# This is a home page where Hello django msg will appear
def home(request):
    return HttpResponse("Hello, Django!!!")


#Simple Python Program to see if a given url input name is ascii value or alphanumeric
# accordingly print message
# for this we need to update url with /hello/name as this is practise page without html
def getData(request, name):

    # getting user’s name     
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + name
    return HttpResponse(content)

#using html page content this function will show current date time 
#tfor this we need to  
def hello_there(request, name):
    return render(
        request,
        'hello/getData.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )