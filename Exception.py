'''try:
    no1=int(input("Enter the number :"))
    no2=int(input("Enter the second number :"))
    print(no1/no2)
except ZeroDivisionError:
    print("Please check the number 2,you can't enter zero,please enter the value form one[1]")
except ValueError:
    print("The two numbers are must be an integer")

finally:
    print("Finally block will be  calling always irrespective whether exception occurs or not.  ")
x=10

try:
    x=print(a)
except NameError:
    print("This class has no attribute a"
class test:
    def __init__(self):
        self.test1='test2'
    def test2(self):
        print(self.test1)
obj=test()

try:
    obj.test4()

except AttributeError:
    print("Test class has no attribute test1")
from tkinter import messagebox as msg
try:
    list=[1,2,3,4]
    print(list[3])
except LookupError:
    print("Array index out of range")
else:
    msg.showinfo("SUCCESS","Successfully completed")
try:
    dict={0:1,1:2}
    print(dict[1])
except LookupError:
    print("Key value error")
try:
    import os
except ImportError:
    print("Import Error")
else:
    print("success")
try:
    no1=int(input("Enter the no1:"))
    no2=int(input("Enter the no2:"))
    try:
        print(no1/no2)
    except ZeroDivisionError:
        print("The second value can't be zero,you must enter an integer from 1 ")
    finally:
        print("inner finaly")
except ValueError:
    print("You must only enter an integer")
finally:
    print("Outer finally")
try:
    no1=int(input("Enter the no1:"))
    no2=int(input("Enter the no2:"))
    print(int(no1/no2))
except:
    print("Exception occurs")
else:
    print('No exception occurs')
finally:
    print('finally got printed')
class ISBException(Exception):
    def __init__(self,msg='Insufficient Balance'):
        self.msg=msg
    def ISB(self):
        print( self.msg )

balance=1000
try:
    amt=int(input("Enter your amount :"))
    if balance<amt:
        raise ISBException()
except ISBException:
    obj=ISBException()
    obj.ISB()
except ValueError:
    obj=ISBException('value Error')
    obj.ISB()

else:
    print('Successfully withdrawn')
    print('your current balance is {}'.format(balance-amt))'''




