'''import os
path=os.path.abspath(__file__)
f=open("input1.txt","w")
list=['Dhivagar','Ram','Arun','Yuva']
f.writelines(list)
print(f.mode)
print(f.writable())
f.close()
f=open('input1.txt','r')
list=f.readline()
for name in list.split():
    print(name)
print(f.name)
print(f.closed)
print(f.mode)
print(f.readable())
f.close()
print(f.closed)
with open('input1.txt','w') as file:
    l1=['dhiva']
    l2=['arun']
    file.writelines(l1)
    file.close()
with open('input1.txt','r') as file:
    data=file.readline()
    print(data)
    file.close()
with open('input1.txt','a')as file:
    l1=['yuva','arun','ram']
    file.writelines(l1)
    file.close()
with open('input1.txt','r') as file:
    data=file.readline()
    print(data)
    file.close()
import os
import sys
filename=input("enter your filename:")
if os.path.isfile(filename):
    print('file is present')
    wordcount=charcount=linecount=space=0
    with open(filename,'r') as file:
        for line in file:
            if line==' ':
                space+=1

            charcount+=len(line)
            words=line.split()
            wordcount+=len(words)
            linecount+=1
            print(line)
        else:
            print(wordcount)
            print(charcount)
            print(linecount)
            print(space)

else:
    print('file is not present')
inputfile=open('pic1.jpg','rb')
output=open('pic2.jpg','wb')
byte=inputfile.read()
output.write(byte)
import csv
with open('student.csv','r',newline='')as file:
    r=csv.reader(file)
    print(r)#csv reader object
    for data in r:
        print(data)
import os
#os.mkdir('ABC')
#os.mkdir('ABC/abc')
#os.makedirs('D/d')
os.removedirs('D/d')'''


