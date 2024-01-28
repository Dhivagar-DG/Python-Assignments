'''import sys
t=('dhivagar',1)
t1=('ram','1')
t2=('arun','1')
print(str(sys.getsizeof(t)))
print(str(sys.getsizeof(t1)))
print(str(sys.getsizeof(t2)))'
#Maximum and minimum
t=eval(input("Enter the tuble"))
n=int(input("Enter the index"))
#t=list(t)
temp=sorted(t)
print(type(temp))
l=[]
#for i,j in enumerate(temp):
 #   if i!=n:
  #      l.append(j)
#l=tuple(l)
res=tuple(temp[:n]+temp[n+1:])
print(type(res))
print(res)
#list of tuple and its cube
n=eval(input("Enter the list:"))
res=[]
for i in n:
    res.append((i,i**3))
print(type(res[0]))
print(res)
#adding list to tuple
t=eval(input("Enter the tuble"))
l=eval(input("Enter the list"))
#for i in t:
 #   l.append(i)
l.extend(t)
print(l)
#sum of tuple elements
t=eval(input("Enter the tuble"))
res=sum(t)
#for i in t:
 #   res+=i
print(res)
#tuple frequency
t=eval(input("Enter the tuple"))
d={}
for i in t:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''
#all pair combination of 2 tiples
t=eval(input("Enter the tuble"))
t1=eval(input("Enter the tuble"))
res=[]
'''for i in t:
    for j in t1:
        res+=[(i,j)]
for i in t:
    for j in t1:
        res+=[(j,i)]'''
res+=[(i,j)for j in t1 for i in t]
res+=[(j,i)for j in t1 for i in t]
print(res)
print(len(res))











