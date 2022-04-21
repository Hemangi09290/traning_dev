from zipfile import ZipFile
import os

def extracting_zipfile():
    print(os.listdir())
    file="Demo.zip"
    "ZipFile constructor; READ mode; ZipFile object named as zip"
    with ZipFile(file,'r') as zip:
        "To print contents of the archive"    
        zip.printdir()                      
        print("Extracting files")
        "Extract contents of the ZIP to the current working directory"
        zip.extractall()                    
    print("Finished extracting")
    
def rights_tofile():
    os.getcwd()
    print(os.listdir())
    txt = open('sample2.txt')
    "To read in binary mode"
    txt=open('Demo.txt','r+b') 
    txt=open('Demo.txt','a')
    txt.close()
    
"To read the contents of python file"
def read_pyfile():
    with open('Demo.txt') as todo:
        todo.read()

"To read specific lines from python file"
def read_specificpylines():
    with open('Demo.txt') as todo:
        todo.read(5)
    
"tell() will tell us where the cursor is rightnow and it gives int values"
def tell_pyfile():
    with open('Demo.txt') as todo:
        todo.read(5)
        todo.tell()

"seek() takes an int argument and sets the cursor at the perticular position"
def seek_pyfile():
    with open('Demo.txt') as todo:
        todo.seek(0)
        todo.read()

extracting_zipfile()
rights_tofile()
read_pyfile()
read_specificpylines()
tell_pyfile()
seek_pyfile()
