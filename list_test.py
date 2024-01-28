'''l=eval(input('enter the list ex:[1,2,3,4,5] : '))
l1=[]
string=''
length=len(l)
for i in range(length):
    for j in range(length):
        string=''
        if i!=j:
            string=str(l[i])+str(l[j])
            print(string,end=' ')
            if int(string)%2!=0:
                l1.append(int(string))
else:
    print(l1)'''
syear=int(input("Enter the starting year :"))
eyear=int(input("Enter the ending year :"))
l1=[]
for i in range(syear,eyear+1):
    if (((i%4==0) and (i%100!=0)) or (i%400==0)):
        l1.append(i)
print(l1)
print('NO of leaf years between {0} to {1}-->{2}'.format(syear,eyear,len(l1)))