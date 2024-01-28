'''import re
pattern=re.compile('[A-Z][a-z]')
input=input('Enter your name:')
if pattern.search(input):
    print('next')
else:
    print('do it correctly')
import re
pattern=re.compile('(0|91)[6-9][0-9]{9}')
no=input('Enter your number:')
if pattern.search(no):
    print('next')
else:
    print('do it correctly')
import re
pattern=re.compile('([6-9][0-9]{4})-([0-9]{5})')
number=input("Enter your number:")
if pattern.search(number):
    print('next')
else:
    print('do it correctly')
#FINDALL
import re
string='Some mobile numbers are 8248205872,7200642002,9876543210'
pattern=re.compile('[6-9][0-9]{9}')
number=pattern.findall(string)
for i in number:
    print(i)
import re
pattern=re.compile('[a-z]{3,20}[0-9]{1,9}[@][gmail.com]')
email=input('Enter your mail-id:')
if pattern.search(email):
    print('next')
else:
    print('do it correctly')
import re
def wordcount(sentence):
    pattern=re.compile('(\s)')
    space=pattern.findall(sentence)
    return len(space)+1
sen=input('Enter your number:')
print(wordcount(sen))
import re
statement=re.sub('[a-z]','$','a1b2c3d4')
print(statement)
import re
def passwordchecker(password):
    if len(password)<8:
        return 'Password should have 8 characters'
    else:
        if re.search("[A-Z]",password)and re.search("[a-z]",password)and re.search("[0-9]",password)and re.search("[@#$_]",password):
            return 'Strong password'
        else:
            return 'Password should have atleast 1 uppercase,lowercase,numeric value,special charecter.'
password=input('Enter your password:')
print(passwordchecker(password))
import re
statement=re.sub('[a-z]','!@#$%^&*()','abcd' )
print(statement)
import re
statement=re.subn('[a-z]','$','a1b2c3d4e5g6')
print(statement)
print(statement[0])
print(statement[1])
import re
lis=re.split('-','chennai-600028')
print(type(lis))
print(lis)
for i in lis:
    print(i)
import re
sentence='Tomorrow is our day'
res1=re.search('day$',sentence)
res1=re.findall('day$',sentence)
res2=re.search('^tomorrow',sentence)
print(res1)
if res1==None and res2==None:
    print('Searched term is not present')
else:
    print("Searched term is present")
import re
file=open('input1.txt','r')
for line in file:
    res=re.search('^From:',line)
    if res!=None:
        sendermail=line.rsplit()
        #print((sendermail))
        email=sendermail[len(sendermail)-1]
        res2=(email.split('>'))
        res3=res2[len(res2)-len(res2)].split('<')
        print(res3[1])
import re
sentence='<dhivagardg07@gmail.com>'
res=sentence.strip('<')
res=res.strip('>')
print(res)
#date pattern
import re
datepattern=re.compile(r'([0-3][0-9])/([0-1][0-9])/((\d){4})')
datefound=datepattern.search('My birthday date is 29/02/2000')
if not datefound is None:
    day=datefound.group(1)
    month=datefound.group(2)
    year=datefound.group(3)
    if month in ['13','14','15','16','17','18','19']:
        print('Invalid month,Month can\'t be greater than 12' )
    else:
        if month in ['01','03','05','07','08','10','12']:
            if int(day)>31:
                print('Invalid date ,date can\'t be greater than 31')
        elif month in ['04','06','9','11']:
            if int(day)>30:
                print('Invalid date,date can\'t be greater than 30')
        else:
            if int(day)>29:
                print('Invalid date,date can\'t be greater than 29')
            elif int(day)==29:
                y=int(year)
                if not (y%4==0 and y%100==0 and y%400==0):
                    print( 'Invalid date,date can\'t be greater than 28' )
else:
    print('Invalid Date')
from collections import Counter as c
sen=input('Enter the sentence : ')
ans=c(sen)# return dict
max=2
st=0
for key,values in ans.items():
    print(key,values)
    if max<values:
        max=values
        st=key
print(st)'''







