'''def outer():
    a=10
    def inner():
        b=10
        return a+b
    return inner
obj=outer()
print(obj())
def outer(fun):
    def inner():
        s=fun()
        return s[::-1]
    return inner
def string():
    s = input( 'enter the string:' )
    return s
obj=outer(string)
print(obj())
def outer(fun):
    def inner():
        n=fun()
        tot=0
        for i in str(n):
            tot+=int(i)
        return tot
    return inner
@outer
def sum1():
    n=int(input('Enter the digit:'))
    return n
print(sum1())'''

