import os,subprocess
import shutil
from threading import Thread

def filehandle_thread():
    "gives current working directory in python"
    print(os.getcwd())
    "gives list of direcories"
    print(os.listdir())
    "using thread we can copy files "
    "here sample2.txt file will remain in the same directory where sample1 txt file is available"
    Thread(target=shutil.copy, args=['sample1.txt','sample2.txt']).start()
    
def filehandle_subproces():
    "gives current working directory in python"
    print(os.getcwd())
    "gives list of direcories"
    print(os.listdir())
    "if we want to change the directory for copy file we can do with os.chdir()"
    "os.chdir('D:\\HEMANGI')"
    "subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)"
    "here args is command i.e. copy and it waits for the cmd to complete then return the statuscode"
    status=subprocess.call('copy sample1.txt sample2.txt', shell=True)
    if status!=0:
       if status<0:
            print(f"Killed by signal {status}")
       elif status>0:
            print(f"Command failed with return code {status}")
       else:
            print("Successfully executed command")
    
def filehandle_shutil():
    "gives current working directory in python"
    print(os.getcwd())
    "gives list of direcories"
    print(os.listdir())
    "if we want to change the directory for copy file we can do with os.chdir()"
    "os.chdir('D:\\HEMANGI')"
    "here only src file and the destination file where want to copy data should be given in arg "
    shutil.copyfile('sample1.txt','sample3.txt')
    
def filehandle_rename():
    os.rename('Python Study', 'Documents')
    print(os.listdir())
    
def multiple_file_rename():
    os.chdir('D:\\HEMANGI\\Documents')
    i=1
    for file in os.listdir():
        src=file
        dst="Dog"+str(i)+".jpg"
        os.rename(src,dst)
        i+=1
    print(os.listdir())

"call all functions here"
filehandle_thread()
filehandle_subproces()
filehandle_shutil()
filehandle_rename()
multiple_file_rename()