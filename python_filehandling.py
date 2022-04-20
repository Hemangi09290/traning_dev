import os
"gives current working directory in python"
print(os.getcwd())
"gives list of direcories"
print(os.listdir())
os.mkdir('Python learning')
print(os.listdir())
os.rename('Python learning', 'Python Study')
print(os.listdir())
print(os.path.exists('D:\HEMANGI'))
print(os.path.isdir('D:\HEMANGI'))
"it gives a file with perticulare read/write mode"
"here command is for the command with action we want to perform"
"mode is for read/write mode bydefault read mode is avail"
"bufsize is for any buffering of space is there or not inform of 0 (means no uffering) and 1 (means line buffering while accesin a file) "
"os.popen(command[, mode[, bufsize]])"
os.chdir('D:\\HEMANGI\\filehandling')
os.popen('copy python_filehandling.txt demo.txt')
