import pickle
class student:
    '''This class is about student'''
    scl='ZKM HR SEC SCHOOL'
    def __init__(self,name,id,address):
        self.name=name
        self.id=id
        self.address=address
    def display(self):
        print(self.name,self.id,self.scl,self.address,sep='  ')

no=int(input('Enter the no.of Students:'))
f=open('abcd.jpeg','wb')
for i in range(no):
    id=int(input('Enter ID:'))
    name=input("Enter name:")
    address=input("Enter Address:")
    stu1=student(id,name,address)
    pickle.dump(stu1,f)
else:
    print('pickeld')
f.close()
f=open('abcd.jpeg','rb')
while True:
    try:
        stu2=pickle.load(f)
        stu2.display()
    except EOFError:
        print('Complited')
        break
if __name__=='__main__':
    print('yes')