# Inheritance is a way to create a new class that inherits all the properties and methods from another class.
# The class that inherits from is called the parent class, and the class that inherits from the parent class is called the child class.
# The child class will have all the properties and methods of the parent class.
# The child class can also have its own properties and methods.
# The child class can also override the properties and methods of the parent class.
# There is no such thing as private and public in Python. All variables and methods are public.
# Every class in Python inherits from the object class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"A person named {self.name} is {self.age} years old."

person = Person("John Doe", 21)

print(Person)
print(isinstance(person, Person))
print(isinstance(person, object))

print(person.__str__())
