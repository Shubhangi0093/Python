# Python
Python_OOPs

#Defining the instance method using an expresion inside a intance method

class Marks:
    
    def __init__(self,name,java,python):
        self.name=name
        self.java=java
        self.python=python
        
    def average(self):
        TotalMarks=(self.java)+(self.python)
        average=(TotalMarks/200)*100
        print("Average of",self.name,"is",average)
          
m1 = Marks("Shubhangi",60,78)
print(m1.name)
print(m1.java)
print(m1.python)

m1.average()
#print(m1.average)

m2 = Marks("Krish",55,64)
print(m2.name)
print(m2.java)
print(m2.python)

m2.average()
#print(m2.average)          
