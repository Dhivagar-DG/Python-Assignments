'''s=input("Enter the string")
s1=''
for x in range(len(s)-1,-1,-1):
    s1+=s[x]
print(s1)
def sod(n):
    if n==0:
        return 0
    else:
        return n%10+sod(n//10)
n=123
print(sod(n))'''





