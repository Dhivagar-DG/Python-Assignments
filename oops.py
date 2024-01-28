'''def marks(**m):
    tot=0
    for i,j in m.items():
        tot+=j
        print(i,j,sep=':')
    return tot/5
if __name__=="__main__":
    print("average :",marks(t=90,e=91,m=92,s=93,ss=100))
def marks(*m):
    #tot=sum(m)
    tot=0
    for i in m:
        tot+=i
        print(i,end=' ')
    print()
    return tot/5
if __name__=="__main__":
    print("average :",marks(90,91,92,93,100))
discount=20
def opentime():
    global discount
    discount=30
    print("Oening Time :",discount)
def tv():
    print(discount)
def labtop():
    discount=25
    print(discount)
    print(globals()['discount'])
opentime()
tv()
labtop()
class student:
    \'''this class is about student\'''
print(student.__doc__)
help(student)
#Instance variable-Dynamic // class variable-Static // local variable
#instance method // class method // static method
#costructor--->constructor is called or invoked whenever we create an object,/special function/Intialising the instance variable
class student:
    \'''This class is about student \'''
    uName='madurai kamaraj university'
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def display(self):
        return self.name,self.dept,student.uName
    @staticmethod
    def addmark(x,y):
        return x+y
    @classmethod
    def check(cls,input1,input2):
        input2=[]
        res=0
        for i in input1:
            res+=i
        else:
            return res,cls.uName



s=student('Dhivagar',"CS")
print(student.__doc__)
help(student)
print(s.display())
input1=[1,2,3,4,5]
input2=[]
print(student.check(input1,input2))
#INHERITANCE
class engine:
    milage=20
    def __init__(self):
        self.petrol=True
    def enginestart(self):
        print("Engine start smoothly")
class car:
    def __init__(self):
        self.engine=engine()
    def drive(self):
        print(self.engine.milage)
        self.engine.enginestart()
c=car()
c.drive()
class rbi:
    \'''this class is about RBI\'''
    name='reserve bank of india'
    name=name.title()
    def __init__(self):
        self.minbal=1000
    def deposit(self):
        print('deposit')
    def withdraw(self):
        print('withdraw')
    @staticmethod
    def s():
        print('static method')
    @classmethod
    def c(cls,x):
        print('class method',x,cls.name)
class sbi(rbi):
    \'''this class is about State bank of india\'''
    #super().__init__()
    name1='state bank of india'
    name1=name1.title()
    def __init__(self):
        super().__init__()
        self.minbal1=500
s=sbi()
print(s.name)
#s.deposit()
#s.withdraw()
#s.s()
#s.c(10)
print(s.minbal)
class student:
    \'''this class is about Student\'''
    name='Madurai Kamaraj University'
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
class exam(student):
    \'''this class is about exam \'''
    def __init__(self,name,dept,examname):
        super().__init__(name,dept)
        self.examname=examname
    def hallticket(self):
        return self.name,self.dept,self.examname,student.name
    def __str__(self):
        return '{} {} {} {}'.format(self.name,self.dept,self.examname,student.name)

e=exam('dhivagar','Msc cs','Python')
print(e.hallticket())
print(e)
#multilevel inheritance
class rbi:
    def __init__(self):
        self.name='rbi'
    def deposit(self):
        print('deposit')
    def withdraw(self):
        print('withdraw')
class sbi(rbi):
    def __init__(self):
        self.name1='sbi'
        super().__init__()
    def eduloan(self):
        print('education loan')
class cobank(sbi):
    def __init__(self):
        self.name2='cobank'
#        super().__init__()

    def agloan(self):
        print('agloan')
    def display(self):
        super().__init__()
        print(self.name,self.name1,self.name2)

c=cobank()
c.agloan()
c.eduloan()
c.deposit()
c.withdraw()
c.display()
#MULTIPLE INHERITANCE
class father:
    def __init__(self):
        self.name='father'
    def fun(self):
        print('father instance method')
class mother:
    def __init__(self):
        self.name='mother'
    def fun(self):
        print('mother instance method')
class child(mother,father):
    def __init__(self):
        self.name='child'
        super().__init__()
    def display(self):
        print(self.name)
        super().fun()
        father.fun(self)

c=child()
c.display()
#@classmethod
class parent:
    i=100 #Class variable
    def __init__(self): #Constructor
        self.j=200   #Instance variable
        print('hi i\'m super class constructor')
    def test(self):
        print('testing in superclass')
    @staticmethod
    def test1():
        print('testing in static method')
    @classmethod
    def test2(cls):
        print('Parent class method')
class child(parent):
    def __init__(self):
        #print(super().i)
        super().__init__()
        #super().test()
        #super().test1()
        #super().test2()
    def display(self):
        print(super().i,self.j)
        super().test()
        super().test1()
        super().test2()
    @classmethod
    def dis(cls):
        print(super().i)
        super(child,cls).test(cls)
        super().test1()
        super().test2()
c=child()
c.dis()
#operator overloading
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
    def __sub__(self, other):
        return self.pages-other.pages
    def __mul__(self, other):
        return self.pages*other.pages
    def __floordiv__(self, other):#__(self, other):
        return self.pages/other.pages
    def __mod__(self, other):
        return self.pages%other.pages
b=book(100)
c=book(200)
print(b+c)
print(c-b)
print(b*c)
print(b//c)
print(b%c)
#method overloading and constructor overloading
class test:
    def __init__(self,*args):
        self.l=[]
        for i in args:
            self.l.append(i)
        print(self.l)
    def calculate(self,**var):
        res=0
        for i in var.values():
            res+=i
        return res
t=test(10,20,30,40,50)
print(t.calculate(x=10,y=40,z=50))
#method overriding and constructor overriding
class parent:
    def __init__(self,*args):
        self.l=[]
        for i in args:
            self.l.append(i)
    def display(self):
        print(self.l)
class child(parent):
    def __init__(self,*args):
        super().__init__(*args)
    def display(self):
        #super().display()
        print(self.l)
c=child(10,20,30)
c.display()'
#Abstarction
#showing only the necessary data and hiding unwanted
#ABC-->Abstract base class
#abc--->First We import abc module ,after that only we can access ABC class.
from abc import *
class car(ABC):
    @abstractmethod
    def color(self):
        pass
class bmw(car):
    def start(self):
        print("CAR STARTED")
    def color(self):
        self.color1='BLACK'
        print(self.color1)
b=bmw()
b.start()
b.color()
from abc import *
class dbinterface(ABC):
    @abstractmethod
    def estabilishdb(self):pass
    @abstractmethod
    def disconnectdb(self):pass
class oracledb(dbinterface):
    def estabilishdb(self):
        print('Oracle db connection')
    def disconnectdb(self):
        print("Disconnect oracle db")
class mysqldb(dbinterface):
    def estabilishdb(self):
        print("MySql db connection")
    def disconnectdb(self):
        print("disconnect my sql")
dbname=input("Enter the dbname:")
classname=globals()[dbname]
c=classname()
c.estabilishdb()
c.disconnectdb()
#Encapsulation
#DATA BINDING
#class variable-->a=10
#instance variable-->self.b=10
#protect variable--> _c=20
#private variable--> __d=30
class test:
    a=100   #Public
    _b=200  #Protected
    __c=300 #private
    def __init__(self):
        self._no1=400
        self.__no2=500
    def display(self):
        self.z=1000
        print(test.a)
        print(test._b)
        print(test.__c)
        print(self._no1,self.__no2,sep=' ')
    def print1(self):
        print(self.z)

t=test()
t.print1()'''
#EXCEPTION HANDLING
n=0
for i in l:
    print(i)


