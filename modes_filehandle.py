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
    
extracting_zipfile()
