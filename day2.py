

# a parent class
class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
    def greet1(self):
        print("Hello" +self.name)
        
        
    def hillo(self):
        print("Hello How are you doing My friend")
        
parent = Parent("Su",30)
# calling the method inside of the class
parent.greet1()


# Inheritance 
# The class is inheriting features from the parent
class Duplicate(Parent):
    
    def greet_you(self):
        
        # as self.name is already defined in the parent class we can easily call it.
        print(f"Hello {self.name}")
  
#we need to provide the attribute of the parameter of "the parent class"   
duplicate = Duplicate("Suman",18)
duplicate.greet_you()
# returns Hello Suman


class Duplicate2(Parent):

    def __init__(self,name,age):
        # super means the parent class
        # Initializing the value of the parent class
        super().__init__(name,age)
        
        
    def greet_you(self):
        print(f"Hello " + self.name)
        # returns the function that is defined in the parent class
        return self.hillo()
        
duplicate2 = Duplicate2( "Suman Bhandari",18  )
duplicate2.greet_you()


class Origin :
    def father_messege(self):
        return"Hello this is origin"
    pass
class V_origin:
    def mother_messege(self):
        return "Hello this is v_origin"
    pass 

# a class can inherit properties from two classes simultaneously 
class Branch(Origin,V_origin):
    def messege(self):
        return f"{self.father_messege()} and {self.mother_messege()}"
    
child = Branch()
print(child.messege())









