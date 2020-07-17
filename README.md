# Python
Python_OOPs
#USing Parameterized Constructor

class Technology:
    
    def __init__(self,cname,cno,cfees):
        self.name=cname
        self.courseno=cno
        self.coursefees=cfees
        
t1=Technology("Java",1,15000)
print(t1.name)
print(t1.courseno)
print(t1.coursefees)

t2 = Technology("Python",2,20000)
print(t2.name)
print(t2.courseno)
print(t2.coursefees)         
    
