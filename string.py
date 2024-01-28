'''#palindrome and Symmetrical
s=input("Enter the String:")
l=len(s)-1
l1=len(s)//2
s1=''
for i in range(l,-1,-1):
    s1+=s[i]
else:
    if  s1==s:
        print("Given String Is Palindrome")
    else:
        print("Not palindrome")
if s[0:l1]==s[l1:]:
     print("symmetrical")
else:
    print("Not symmetrical")
#reverse the words in a given string
s=input("Enter the sentence")
s1=s.split()
print(s1)
l=len(s1)-1
s2=[]
for i in range(l,-1,-1):
    s2.append(s1[i])
else:
    print(' '.join(s2))
#remove ith char
s=input("Enter the string:")
n=int(input("Enter the position:"))
s1=''
for i in range(0,len(s)):
    if i!=n:
        s1+=s[i]
print(s1)
s1=s.replace('a','',2)
print(s1)
#AVOID SPACES in string length
s=input("enter the string:")
s1=s.replace(' ','')
l,l1=0,0
for i in s1:
     l1+=1
for i in s:
    if not i.isspace():
        l+=1
print(l,l1,sep=':')
#print even length words in a string
s=input("Enter the string:")
s1=s.split()
for i in range(0,len(s1)):
    if i%2==0:
        print(''.join(s1[i]),end=' ')
#Uppercase half a char
s=input("Enter the string:\t")
mid=len(s)//2
s1=''
for i in range(0,len(s)):
    if i>=mid:
        s1+=s[i].upper()
    else:
        s1+=s[i]
print(s1)
#Captialize first and last character upper *************************PENDING**************************
s=input("Enter the string:")
s1=s.split()
s2=[]
s3=[]
for i in range(len(s1)):
    s2.append(s1[i].title())
    s2=s1[i][0:len(s1[i])-1].title(),s2[i][-1].upper()

else:
    print(' '.join(s2))
#Check one letter and one number
s=input("Enter the string:")
val=False
val1=False
for i in s:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        val=True
    if i>='0' and i<='9':
        val1=True
else:
    if val==True and val1==True:
        print("CRT")
    else:
        print("NOt")
#Check Vowels
s=input("Enter the string:")
v={'a','e','i','o','u'}
s1=set()
c=0
for i in v:
    #if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
    #    s1.add(i)
   # if i in v:
    #    s1.add(i)
    s1=(set(s.lower()).intersection(v))
    if s.count(i)>=1:
        c+=1
else:
    print(s1)
    if len(s1)==len(v):
        print('crt')
    else:
        print('NOT')
if c==len(v):
    print('crt')
else:
    print("not")
#MATCHING char
s=input("Enter the string:")
s1=input("Enter the string:")
s3=''
#min=min(s,s1)
#max=max(s,s1)
if s>s1:
    max=len(s)
    min=len(s1)
else:
    max=len(s1)
    min=len(s)
c=0
for i in range(min):
    c+=1
    for j in range(max):
        if i==j:
            s3+=s[i]
print(s3,len(s3),sep=':')
print(c)
#NO OF VOWELS
s=input("Enter the string:")
v={'a','e','i','o','u'}
c,c1=0,0
for i in v:
    if s.count(i)>=1:
        c+=1
for i in set(s):
    if i in v:
        c1+=1
print(c,c1,sep=' : ')
#remove all duplicates from a string
s=input("Enter the string:")
s1=''
for i in s:
    if i not in s1:
        s1+=i
print(s1)
#LEAST FREQUENT CAHR
s=input("Enter the string:")
s1={}

for i in s:
    if i in s1:
        s1[i] +=1
    else:
        s1[i]=1
min2=s1.values()
min1=min(min2)
for i,j in s1.items():
    if j==min1:
        print(i,end=' ')'
#Maximum frequent value
s=input("Enter the string:")
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
max1=max(d.values())
for i,j in d.items():
    if j==max1:
        print(i,end=' ')'
#ODD and even frequency
s=input("Enter the string:")
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[]
for i,j in d.items():
    if j%2==0 and not str(j).isspace():
        l.append(i)
print(l)
#Specific Frequency
s=input("Enter the String:")
s1=input("Enter the specific char:")
d={}
for i in s1:                        #da
    for j in s:                     #dhivagar dhivagar
        if i==j:                    #1.d==d-->d not in d -> d:1 d==d d not in d else:d:1+1-->d:2X
            if i not in d:          #2a d==a x a==a-->a not in d -->d[a]=1 g==a a==a-->a not in a-->else:d[a]+=1=2....
                d[i]=1
            else:
               # if i==j:
                d[i]+=1

print(d)
#Frequency of numbers in string:
import re
s=input("Enter the string:")
res=(re.findall(r'\d+',s))
print(len(res))
#Check special char
s=input("Enter the String")
val=True
for i in s:
    if i.isalpha():
        continue
    elif i.isdigit():
        continue
    else:
        val=False

if val==False:
    print("String Not accepted")
else:
    print("String accepted")
import re
regex=re.compile('[!@#$%^&*(){}|\":?></~`]')
if re.search(regex,s)==None:                    #########Search return None or TRUE
    print("String Accepted")
else:
    print("String Not Accepted")
#Graeter than given lenght k#remove Ith char
s=input("Enter the sentence:")
s1=s.split()
k=int(input("Enter the Length"))
for i in s1:
    if len(i)>k:
        print(i,end=' ')
print()
s2=''
for i in range(len(s)):
    if i!=k:
        s2+=s[i]
print(s2)
#Split and join
s=input("Enter the sentence:")
s1=s.split()
print(s1)
s2='-'.join(s1)
print(s2)
#Check Binary string
s=input("Enter the sentence:")
s1=set(s)
s2={'0','1'}
if s1==s2 or s1=={'0'} or s1=={'1'}:
    print('yes')
else:
    print('No')
#Find all close matches
s=input("Enter the sentence:")
s2=input("Enter the sentence:")
s2=set(s2)
s1=s.split()
s3=[]
for i in s1:
    if set(i).issubset(s2):
        s3.append(i)
print(s3)'''
#Uncommonn words
s=input("Enter the sentence:")
s1=input("Enter the sentence:")
s2=[]
if len(s.split())>len(s1.split()):
    for i in s.split():
        if i not in s1.split():
            s2.append(i)
else:
    for i in s1.split():
        if i not in s.split():
            s2.append(i)
print(s2)

























