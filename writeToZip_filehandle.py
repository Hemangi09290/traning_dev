from zipfile import ZipFile
import os

"using this function, we can write(add,del,update txt files) files to zip folder"
"here we need Python Study folder and txt files in it otherwise it can give error like no folder avail"
"and DemoFile.zp folder should not have that txt files in it "
"so now using this function we can write into DemoFile.zip -> Python Study -> txt files"
def writeTo_zipfile(directory):
    paths=[]
    print(directory)
    for root, directories, files in os.walk(directory):
        for filename in files:
            print(files)
            filepath=os.path.join(root,filename)
            paths.append(filepath)
    return paths

directory='.\Python Study'
paths=writeTo_zipfile(directory)
print(paths)
print("Zipping these files:")
for file in paths:
    print(file)
    with ZipFile('DemoFile.zip','w') as zip:
        for file in paths:
            zip.write(file)
print("Zip successful")


"output for this:"
".\Python Study"
"['1.txt', '2.txt']"
"['1.txt', '2.txt']"
"['.\\Python Study\\1.txt', '.\\Python Study\\2.txt']"
"Zipping these files:"
".\Python Study\1.txt"
".\Python Study\2.txt"
"Zip successful"

