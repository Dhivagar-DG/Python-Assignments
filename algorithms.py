'''#********************BINARY SEARCH ************BUBBlE SORT
l=eval(input("ENTER THE LIST:"))
#l=[10,20,30,40,50]
key=int(input("ENTER THE SEEARCH KEY:"))
length=len(l)-1
for i in range(0,length):
    for j in range(0,length-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

min=0
max=len(l)-1
while min<=max:
    mid=(min+max)//2
    if l[mid]==key:
        print("{} is present at {}".format(key,mid+1))
        break
    elif key>l[mid]:
        min=mid+1
    else:
        max=mid-1
else:
    print("{} not present at in this list".format(key))'''
import numpy as np
np.arange(1,10)