 # creating a blue print of an object
class Student():
    pass

# creating a instance of a class
new_student = Student()

new_student.name = "Suman Bhandari"
new_student.grade = "XI"

print(new_student)
# <__main__.Student object at 0x10041fc10>
# Is the location where my class is located

# Classes are used to model the real world objects like Student or human(common noun)
class Human():
    
    # Creating a constructor that holds the value of the common property that each object have but with different value
    def __init__(self, gender,age,nationality):
        
        # Initiallizing the values
        
        self.gender = gender
        self.age = age 
        self.nationality = nationality 
        
    def __str__(self):
        print(f"Hello This is me from {self.nationality} ")
        
        
        
a_human = Human("Male",18,"Nepal")
print(a_human.__str__())


# Conditional inside a class 
# You can go inside if only you are above 18 and vegetarian

class Person():
    
    def __init__(self,name,isVeg,age,gender):
        self.name = name
        self.isVeg = isVeg
        self.age = age
        self.gender = gender
    
    # check the gender of the Person
    def gender(self):
        if self.gender == "Male":
            return "Mr."
    
        elif self.gender == "Female":
            return "Ms."
    
        else:
            return "Mr./Ms."
        
    # Function inside a class is known as method  
    def isAllowed(self):
        
        if self.age >18 and self.isVeg == True:
        # we can only access the method using self keyword in class
            return f"You are allowed to enter inside {self.name}"
            
        else:
            return f"You are not allowed to enter inside. Hope you understand {self.name}"
        
        
#creating the object with different qualities  
person1 = Person("Suman Bhandari",False,18,"Male")
person2 = Person("Bidhana Bhandari",True,19,"Male")

# calling the method
print(person1.isAllowed())
