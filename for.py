#for no in range(3):
 #   print(no)
#for no in range(5,0,-1):
 #   print(no)
#no=int(input("Enter the Number:"))
#for i in range(1,no+1):
#    print("*"*i)
'''s="python is very very easy"
#print(s.find('s'))
#print(s.rfind('s'))
pos=-1
count=0
length=len(s)
print(id(s))
while True:
    pos=s.find('z',pos+1,length)
    if pos==-1:
        break
    count+=1

    print('very is present at:',pos)
print("COUNT=",count)
s2=s.replace('p','k')
print(id(s2))
print(s)
print()
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize()
s1,s2='DHIVAGAR','MURUGAN'
if len(s1)<len(s2):
    pass
#1234567890
names=['ram','Arun','Karthick','Dhiva']
time=[18,22.3,19.1,17.2]
temp=[]
for i in range(len(names)):
    for j in range(len(time)):
        if time[i]<time[j]:#18<22.3
          #  print(time[i],time[j],sep=':')
            temp=names[i],time[i]
            names[i],time[i]=names[j],time[j]
            names[j],time[j]=temp[0],temp[1]

i=1
for x in range(len(names)):
    print("{} is {} and TIME : {}".format(names[x],i,time[x]))
    i+=1
input='A55B100C7D88E1'
i,j=0,0
while i<len(input):
    m,count=0,1
    while j<len(input)-1:
        j+=1
        if input[j].isnumeric():
            m=(m*10)+int(input[j])
            count+=1
        else:
            break
    #print(j,m)
    print(input[i]*m)
    i+=count
no=int(input())
#no1=64#--A
no1=96#--a
print(chr(no1+no))
list=[10,20,30,20]
sen=input("Enter a sentence:")
l=sen.split()
print(type(l))
s=' '.join(l)
print(type(s))
list=[[1,2,3],[4,5,6],[7,8,9]]
s=0
i=len(list[0])-1
for row in range(len(list)):
    for col in range(len(list[row])):
      #  print(list[col][row] ,end=' ')
        if  col==i:
           print(list[row][col],end=' ')
           s+=list[row][col]
           i-=1

    print()
print(s)'''
a,b,c,d=1,2,3,4
l=[10,20,30,40]
t=a,b,c,d
t1=(j*j for j in range(1,6))
for x in t1:
    print(x,end=' ')
print(t1)
print(t)
print(*t)
