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
#for this we need to  
def hello_there(request, name):
    return render(
        request,
        'hello/getData.html',
        {
            'name': name,
            'date': datetime.now(),
        }
    )

#this is a List example
def getList(request):
    numbers_list = [1,2,3,4]
    content ="Sample demo of List\r\n"
    result = ""
    for i in numbers_list:
        if i%2==0:
            result += content + "\r\n " +f"{i} is composite\r\n"
        else:
            result += content + "\r\n " +f"{i} is not composite\r\n"
    return HttpResponse(result)

#this is a dictionary example
def getDict(request):
    #animals = (([1,'dog'],[2,'cat'],[3,'lion']))
    animals = {'1':'dog', '2':'cat', '3':'lion'}
    animals['4']='tiger'
    result = ""
    for k, v in animals.items():
        result += "index : " + k  + "value : " +  v + "<br /> "
   
    return HttpResponse("Dictionary data <br />" +result)