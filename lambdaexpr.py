import os

def simple_lambda(a=2,b=3):print(a,' ',b)

simple_lambda()
simple_lambda(3)

def assignlambda_call():
    o=lambda x=1,y=2,z=3:x+y+z
    "here 2 pass as arg x and 3 pass as arg of y so x=2 y=3 and z is already there as 3 so oupput should be 8"
    print(o(2,3))

"here for lambda we can omit argument but can't omit expression"
def lambda_withoutarg():
    y=lambda :2+3
    print(y())
    
"use of filter fun for lambda"      
def filter_lambda():
    numbers=[0,1,2,3,4,5,6,7,8,9,10]
    print(list(filter(lambda x:x%3==0,numbers)))
    
assignlambda_call()
lambda_withoutarg()
filter_lambda()