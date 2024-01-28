#SUM OF DIGIT
#RECURSION
'''def sum1(n):
    if(n==0):
        return 0
    return n%10+sum1(n//10)
#WITHOUT RECURSION
def sum2(n):
    if n==0:
        return 0
    s=0
    while(n>0):
        rem=n%10
        s+=rem
        n//=10
    return s

n=int(input("ENTER the VALUE:"))
res=sum1(n)
print("\n{0} SUM OF DIGIT IS {1}".format(n,res))
#FACTORIAL
#RECURSION
def fact(n):
    if n>=0:
        if n==0 or n==1:
            return 1
        return n*fact(n-1)
    else:
        return 0
#WITHOUT RECURSION
def fact1(n):
    if(n>=0):
        if(n==0 or n==1):
            return 1
        s=1
        for i in range(1,n+1):
           s*=i
        return s
    return 0
def fact2(n):
    if(n<0):
        return 0
    elif(n==0 or n==1):
        return 1
    else:
        s=1
        while(n>0):
            s*=n
            n-=1
        return s
n=int(input("ENTER the VALUE:"))
print("\n{0} FACTORIAL IS {1}".format(n,fact2(n)))
#SIMPLE INTEREST
def si(p,t,r):
    return (p*t*r)/100
def ci(p,t,r):
    a=p*(pow((1+r/100),t))
    return a-p
p=float(input("\nENTER THE PRINCIPAL AMOUNT:"))
t=float(input("\nENTER THE TIME:"))
r=float(input("\nENTER THE RATE:"))
print("\n",si(p,t,r))
print("\n",ci(p,t,r))
#ARMSTRONG NUMBER
def order(x):
    n=0
    while(x!=0):
        n+=1
        x//=10
    return n
def isarmstrong(x):
    n=order(x)
    temp=x
    sum1=0
    print(n)
    while(temp>0):
        rem=temp%10
        sum1+=rem**n
        temp//=10
    return sum1
x=int(input("ENTER THE N VALUE:"))
res=isarmstrong(x)
if(x==res):
    print("{0} is an ARMSTRONG NUMBER".format(x))
else:
    print("{0} is not a ARMSTRONG NUMBER".format(x))
#AREA OF CIRCLE
def findarea(r):
    pi=3.142
    return pi*(r**2)
v=int(input("\nENTER THE NUMBER:"))
print("Area of circle is %.2f"%findarea(v))
#PRIME NUMBER
def prime(s,e):
    for i in range(s,e+1):
        if i>0:
            for j in range(2,(i//2)+1):
                if(i%j==0):
                    break
            else:
                print(i)
        else:
            print("{0} is not a prime number",i)


def prime1(s):

    for i in range(2,(s//2)+1):
        if(s%i==0):
            print("{0} is not a prime number".format(s))
            break
    else:
        print("{0} is a prime number".format(s))


s = int( input( "ENTER THE STARTING NUMBER:" ) )
e = int( input( "\nENTER THE ENDING NUMBER:" ) )
prime(s,e)
prime1(s)
#FIBONACCI
n=int(input("ENTER THE NUMBER"))
f1=0
f2=1
f3=0
#print(f1)
#print(f2)
while(n>0):
    f3=f1+f2
    f1=f2
    f2=f3
    if(f3<n):
        pass
       # print(f3)

for i in range(1,n-1):
    f3=f1+f2
    f1=f2
    f2=f3
    print("{0}={1}".format(i,f3))
def fib(n):
    if(n<=1):
        return n
    else:
        return ( fib(n-1)+fib(n-2))
for i in range(0,n+1):
    if(n==i):
        print(i,fib(i))
    else:
        print("{0} = {1}".format(i,fib(i)))
#ARRAY AFTER ROTATION
def leftrotatearray(arr,n,d):
    temp=[]
    i=0
    while(i<d):
        temp.append(arr[i])
        i+=1
    i=0
    while(d<n):
        arr[i]=arr[d]
        i+=1
        d += 1
    arr[:]=arr[:i]+temp
    return arr
d=int(input("ENTER THE NUMBER OF ROTATION:"))
arr=[]
arr=[1,2,3,4,5,6,7]
print("Array After Rotation is:",end='')
print(leftrotatearray(arr,len(arr),d))
#FIND REMINDER OF ARRAY MULTIPLICATION
def findrem(arr,n):
    mul=1
    for i in arr:
        mul*=i%n
    return mul%n
n=int(input("ENTER THE N VALUE:"))
arr=[100,10,5,25,35,14]
print(findrem(arr,n))
#CHECK MONOTONIC
def ismono(arr):
    return all(arr[i]<=arr[i+1] for i in range(len(arr)-1)) or all(arr[i]>=arr[i+1] for i in range(len(arr)-1))
arr=[100,15,15,5]
print(ismono(arr))
#LLLLLLLLLLLIIIIIIIIIIIIIIIIIIIISSSSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTTTTTTTTT
#SWAP
l=[1,2,3,4,5]
n=len(l)
t=l[0]
l[0]=l[n-1]
l[n-1]=t
l[0],l[-1]=l[-1],l[0]
print(l)
s,*m,e=l
l=[e,*m,s]
print(l)
def swap(arr,s,e):
    arr[s],arr[e]=arr[e],arr[s]
    return arr
l=[1,2,3,4,5]
s=int(input("ENTER THE STARTING POSITION:"))
e=int(input("ENTER THE ENDING POSITION:"))
print(swap(l,s,e))
se=int(input("SEARCH ELEMENT:"))
if se in l:
    print("true")
else:
    print("false")
for i in range(0,len(l)):
    if(l[i]==se):
        print("FOR TRUE")
        break
else:
    print("false")
l2=list(l)
print(l2)
#l2.clear()
#l2*=0
del l2[:]
print(l2)
#l.reverse()
#l=l[::-1]
def r(l):

    return [ele for ele in reversed(l)]
print(r(l))
s=0
for x in l:
    s+=x


print(s)
sm=1
for y in range(len(l)):
    sm*=l[y]
print(min(l))
min_=l[0]
for x in l:
    if x>min_:
        min_=x

#print(min_)
#l.remove(max(l))
#print(max(l))
#l.append(5)
#print(l)
l.sort()
print(l[1])
#MATRIX
def add(a,b,res):
    for r in range(len(a)):
        for c in range(len(a[0])):
            res[r][c]=a[r][c]+b[r][c]
    return res
def sub(a,b,res):
    for r in range(len(a)):
        for c in range(len(a[0])):
            res[r][c]=a[r][c]-b[r][c]
    return res
def mul(a,b,res):
    for r in range(len(a)):
        for c in range(len(b[0])):
            for m in range(len(b)):
                res[r][c]+=a[r][m]*b[m][c]
    return res
def prod(a):
    res=1
    for i in a:
        for j in i:
            res*=j
    return res
def transpose(a,res):
    for i in range(len(a[0])):
        for j in range(len(a)):
            res[i][j]=a[j][i]
    return res
def create(n):
    res=[list(range(1+n*i,1+n*(i+1)))for i in range(n)]
    return res
def print1(res):
    for i in res:
        print(i)
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n=int(input("Enter the DIMENSIONS:"))
#print1(create(n))
for i in a:
    print(i[n])

ans=add(a,b,res)
print1(ans)
ans1=sub(a,b,res)
print1(ans1)
ans2=mul(a,b,res)
print1(ans2)


#ans=transpose(a,res)
#print1(ans)
#zip
#res=zip(*a)
#print1(res)
#STRING
a="amma"
n=len(a)
b=a
m=0
for i in range(n):
    if(a[i]==a[n-i-1]):
      m+=1
if(n==m):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
def palindrome(x):
    return x==x[::-1]
def symmetric(x):
    n=len(x)
    if n%2:
        if x[0:n//2]==x[n//2:]:
            return True
    else:

    return False
s="dhivadhivadhiva"
if palindrome(s)==True:
    print("{0} is PALINDROME.".format(s))
else:
    print("{0} is not PALINDROME.".format(s))
if symmetric(s)==True:
    print("{0} is Symmetric".format(s))
else:
    print("{0} is not Symmetric".format(s))
def rev(s):
    x=s.split(' ')
    return ' '.join(reversed(x))
s='DHIVAGAR . M NAME:'

print(rev(s))
n=2
def rem(n,s):
    x=''
    for i in range(len(s)):
        if i!=n:
            x+=s[i]
    return x
t=[]#0-1+2..
t=s[:n]+s[n+1:]
print(t)

#print(r(n,s))
import re
s='Dhivagar'
s1=input("Enter the substring")
def f(s,s1):
    if(s.find(s1)==-1):
        print("no")
    else:
        print("yes")
def c(s,s1):
    if s.count(s1)>0:
        print("yes")
    else:
     print("no")
def r(s,s1):
    if re.search(s1,s):
        print("true")
    else:
        print("no")
f(s,s1)
c(s,s1)
r(s,s1)
import string
s='dhivagar_dhiva_dhiva'
res=s.replace('_'," ").title().replace(" ",'')
print(res)
s='this is python language , i am dhiva'
for i in s.split():
    if len(i)%2==0:
        print(i)
s='dateio'
s1=set()
v='aeiou'
for i in s:
    if i in v:
        s1.add(i)
print(s1)
if(len(s1)==len(v)):
    print('yes')
else:
    print('no')
s='dhiva_dhiva dhiva is ab gar gar gar'
res={i:s.count(i) for i in s.split()}
for key,val in res.items():
    print(key,val)
print(s.replace('_'," ").title().replace(" ",''))
for i in s.split():
    if len(i)%2==0:
        print(i)
v='aeiou'
s='dhivagareoaeiou'
s1='aeiou'
a=set()
for i in s:
    if i in v:
        a.add(i)
print(a)
if(len(v)==len(a)):
    print('true')
else:
    print('false')
a='abcd 5 dab'
b='abcd 5 dabnnmmjk'
s=set()
c=0
for i in a.split():
    if b.count(i)>0:
        c+=1
        s.add(i)

print(c)
s1=''
s1=set(str(a.replace(' ','')))
print(str(s1)
#binary to decimal
import math
m=input("Enter the number:")
n=int(m)
res,rem,i=0,0,0
while n>0:
    rem=n%10
    res+=int(math.pow(rem*2,i))
    n//=10
    i+=1
else:
    print("{} DECIMAL VALUE IS {}".format(m,res))
#DECIMAL TO BINARY
n=int(input("Enter The NUmber:"))
rem,res=0,''
while n>=1:
    rem=n%2
    res=str(rem)+res
    n//=2
else:
    print(res)
#TEST
name=input("ENTER YOUR NAME:")
i=0
rem,res=0,''
val=0
while i<len(name):
    val=ord(name[i:i+1])
    while val>=1:
        rem = val % 2
        res = str( rem ) + res
        val //= 2
    i+=1
else:
    print(res)
import numpy as np
import pandas as pd
lst='d h i v a'.split()
pd.series(lst)
def arm(num):
    l=len(str(num))
    res=0
    while num>0:
        res+=(num%10)**l
        num//10
    return res
n=int(input("Enter the number:"))
if n==arm(n):
    print('{} is Armstrong number'.format(n))
else:
    print('{} is not Armstrong number'.format(n))
#TEST
name=input("ENTER YOUR NAME:")
i=0
rem,res=0,''
val=0
while i<len(name):
    val=ord(name[i])
    while val>=1:
        rem = val % 2
        res = str( rem ) + res
        val //= 2
    i+=1
else:
    print(res)
print(ord('a'))
n=input("Enter the string:")
s=''
for i in range(len(n)):
    if i==len(n)//2:
        s+=n[i].upper()
    else:
        s+=n[i]
print(s)'''
s=input("Enter the string:")
v={'a','e','i','o','u'}
s1=0
count=0
for i in set(s.lower()):
    if i in v:
        count+=1


else:
    s1=set(s.lower()).intersection(v)
    print( s1 )
    if len(v)==len(s1):
        print('crt')
    else:
        print('false')
















