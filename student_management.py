#!/usr/bin/env python
# coding: utf-8

# In[14]:


class student:

    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2 
    
    def accept(self,name,rollno,marks1,marks2):
        obj= student(name,rollno,marks1,marks2)
        a.append(obj)
        
        
        
    def display(self,obj):
        print("name is:",obj.name)
        print("roll no:",obj.rollno)
        print("marks for subj1",obj.marks1)
        print("marks for subj2",obj.marks2)
        print("\n")
              
              
    def search(self,rn):
        for i in range (a.__len__()):
            if(a[i].roll_no == rn):
                return i
    def delete(self,rn):
        i = obj.search(rn)
        del a[i]
        
    def update(self,rn,no):
        i= obj.search(rn)
        roll=no
        a[i].roll_no = roll
        
a=[]
obj1 = student('',0,0,0)
print("Student Data Management")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
ch = int(input("enter choice:"))
if (ch==1):
    obj1.accept("A", 1, 100, 100)
    obj1.accept("B", 2, 90, 90)
    obj1.accept("C", 3, 80, 80)
elif(ch == 2):
    print("\n")
    print("\nList of Students\n")
    for i in range(a.__len__()):
        obj1.display(a[i])
elif(ch == 3):
    print("\n Student Found, ")
    s = obj1.search(2)
    obj1.display(ls[s])

elif(ch == 4):
    obj1.delete(2)
    print(a.__len__())
    print("List after deletion")
    for i in range(a.__len__()):
        obj1.display(a[i])

elif(ch == 5):
    obj1.update(3, 2)
    print(a.__len__())
    print("List after updation")
    for i in range(a.__len__()):
        obj1.display(a[i])
else:
    print("Thank You !")
        
        
        
        
        
        

