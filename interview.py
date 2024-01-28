'''class Calculate(object):
    @classmethod
    def findFeet(cls,input1,input2):
        sum=0
        feet=0
        for i in input2:
            if i>10:
                feet=i//12
                print(i,'-->',feet)
                sum+=feet
           #feet=0
        else:
            return sum
input1=5
input2=[18,11,27,12,14]
feet=Calculate()
print(feet.findFeet(input1,input2))
#REVERSE A STRING
string=input("Enter the string:")
rev=''
for i in range(len(string)-1,-1,-1):
    print(string[i],end='')
print()
print(string[::-1])
for i in reversed(string):
    print(i, end='')
print()
if string==string[::-1]:
    print('{} is palindrome.'.format(string))
else:
    print('{} is not palindrome'.format(string))
#Reverse a number
num=int(input("Enter the number:"))
rev=0
num1=num
while(num>0):  #12345
    rev=rev*10+num%10
    num//=10
print(rev)
if num1==rev:
    print('{} is palindrome.'.format(num1))
else:
    print("{} is not palindrome".format(num1))
#prime number
n=int(input("Enter the number:"))
for i in range(2,n//2+1):  #2--5--->2 to 4
    if n%i==0:
        print('{} is not a prime number'.format(n))
        break
else:
    print( '{} is  a prime number'.format( n )
#N prime number
n=int(input("Enter the range:"))
lst=[]
for i in range(2,n+1):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        lst.append(i)
else:
    print(lst)
    print(len(lst))
#leap year or not
year=int(input("Enter the year:"))
if (year%4==0 and year%100!=0)or(year%400==0):
    print('{} is leap year'.format(year))
else:
    print('{} is not leap year'.format(year))
#Greatest among 10 numbers
lst=[1,2,3,4,5,6,7,8,9,10]

max1=lst[0]
for i in lst:
    if max1<i:
        max1=i
else:
    print(max1)
print(max(lst))
print(min(lst))
#fibonaci series
n=int(input('Enter the limit:'))
f1,f2=-1,1
for i in range(n):
    print(f1+f2)
    f2=f1+f2    #-1+1=0 #1 #1
    f1=f2-f1    #0--1--0+1=1 #0 #1
#factorial
n=5
s=1
for i in range(1,n+1):
   s*=i
print(s)
#HCF
def hcf(x,y):
    res=0
    small=x if x>y else y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            res=i
    else:
        return res
print(hcf(54,12))
#LCM
def lcm_(x,y):
    res=0
    big=x if x>y else y
    while(True):
        if ((big%x==0) and  (big%y==0)):
            res=big
            break
        big+=big
    return res
a=lcm_(3,4)
print(a)
#Armstrong number
n=int(input('enter the number:'))
r=len(str(n))
t=n
res=0
while n>0:
    res+=(n%10)**r
    n//=10
print(res)
if res==t:
    print('Armstrong Number')
else:
    print('Not Armstrong number')
#N Armstrong number
n=int(input("Enter the range:"))
t=0
l=0
lst=[]
for i in range(1,n+1):
    t=i
    res=0
    l=len(str(i))
    while(i>0):
        res+=(i%10)**l
        i//=10
    else:
        if t==res:
            lst.append(t)
else:
    print(lst)
#Decimal  to binary
def deci(n):
    res=''
    while(n>0):
        res=str(n%2)+res
        n//=2
    return res
n=int(input("Enter the decimal number:"))
print(deci(n))
#binary to decimal
import math
def bin1(n):
    res,rem=0,0
    i=0
    while n>0:
        rem=n%10
        res+=rem*(math.pow(2,i))
        n//=10
        i+=1
    return res

n=int(input("Enter the binary value:"))
print(bin(n))
print(bin1(n))
#swap 2 numbers
a=10
b=20
print(a,b)
a+=b
b=a-b
a-=b
print(a,b)
str1='DHIVA'
str2='MURUGAN'
i,j,res=0,0,''
while len(str1)>i or len(str2)>j:
    if len(str1)>i:
        res+=str1[i]
        i+=1
    if len(str2)>j:
        res+=str2[j]
        j+=1
print(res)
#AVG
lst=[10,20,30,40,50]
tot=0
for i in lst:
    tot+=i
print(tot)
print('average=',tot/len(lst))
#sum of digits
n=int(input('Enter the number:'))
s=0
t=n
while n>0:
    s+=n%10
    n//=10
print(s)
s=1
n=t
for i in range(len(str(n))):
    s*=n%10
    n//=10
print(s)
#odd and even
n=int(input("enter the range:")) b
even=[]
odd=[]
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even Number:',even,'\nOdd Number',odd)
#area of circle and circumference of circle
pi=3.14
def area(r):
    return pi*r**2
def circium(r):
    return 2*pi*r
print(area(5))
print(circium(5))
str1='A55b66c5d66'
i,j=0,0
while i<len(str1):
    count,n=1,0
    while j<len(str1)-1:
        j+=1
        if str1[j].isnumeric():
            n=(n*10)+int(str1[j])
            count+=1 #3
        else:
            break
    print(str1[i]*n)
    i+=count
#Strong number
n=145
rem=0
t=n
l=[]
while n>0:
    rem=n%10
    s=1
    for i in range(1,rem+1):
        s*=i
    l.append(s)
    n//=10
print(sum(l))
print(l)
if t==sum(l):
    print('strong number')
else:
    print('not strong number')
#N-Strong number
n=int(input('enter the range:'))
rem=0
l=[]
st=[]
t=0
for i in range(1,n+1):
    t=i
    while i>0:
        s=1
        rem=i%10
        for j in range(1,rem+1):
            s*=j
        l.append(s)
        i//=10
    if t==sum(l):
        st.append(t)
    l.clear()
print(st)
#perfect number
n=int(input("Enter the number:"))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(s,'Strong number')
else:
    print('not')
#N perfect number
n=int(input('Enter the range:'))
l=[]
t=0
s=0
for i in range(1,n+1):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        l.append(i)
    s=0
print(l)
#N neon number
n=int(input('Enter the range:'))
l=[]
s=0
for i in range(1,n+1):
    sq=i*i
    while sq>0:
        s+=sq%10
        sq//=10
    if s==i:
        l.append(i)
    s=0
print(l)'''


















