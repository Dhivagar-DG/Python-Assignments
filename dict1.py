#d=eval(input("Enter the dictionary:"))
#print(d)
s=input("Enter the word:")
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)
l1=[]
l2=[]
l3=[]
l4=[]
for x,y in d.items():
    l1.append(x)
    if y>=2:
        l2.append(x)
    elif y==1:
        l3.append(x)
    l4.append(y)
print(l1)
print(l2)
print(l3)
for  x,y in d.items():
    if y==max(l4):
        print(x,y)





