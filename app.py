print('hello')
str1 = 'hi'
print('to be printed: {}'.format(str1))

'''
class dog:
    def __init__(self,name):
        self.name = name
        print('object with name: {} created'.format(self.name))
        print('object with name: {} created'.format(name))

    def talk(self):
        print('Woof')

    def printName(self):
        print('Na peru: {}'.format(self.name))

    def __str__(self):
        #print('coming from  __str__:',self.name)
        return self.name

obj1 = dog('GreyHound')
obj2 = dog('Dobberman')
obj1.talk()
obj1.printName()
obj2.talk()
obj2.printName()
print('\n\n')
print(obj1)
print(obj2)


## Inheritance(Video 5)
class Person:
    def __init__(self,name):
        self.name = name

    def sayName(self):
        print(self.name)

class Engineer(Person):
    def __init__(self,name):
        super().__init__(name)
        self.proffession = 'Engineer'
    
    def sayProffession(self):
        print(self.proffession)

class Doctor(Person):
    def __init__(self,name):
        super().__init__(name)
        self.proffession = 'Doctor'
    
    def sayProffession(self):
        print(self.proffession)

engineer = Engineer('John')
engineer.sayName()
engineer.sayProffession()

doctor = Doctor('Jane')
doctor.sayName()
doctor.sayProffession()


# dummy class with nothing inside
class A:
    def __init__(self):
        pass

obj = A()

# Multiple Inheritance
class A:
    def printA(self):
        print('From A')

class B:
    def printB(self):
        print('From B')

class C(A,B):
    def printC(self):
        print('From C')

obj = C()
obj.printA()
obj.printB()
obj.printC()


# Multi-level Inheritance
class A:
    def printA(self):
        print('From A')

class B(A):
    def printB(self):
        print('From B')

class C(B):
    def printC(self):
        print('From C')

obj = C()
obj.printA()
obj.printB()
obj.printC()


# Funtion Overriding
class Base:
    def add(self,a,b):
        return a+b

class Derived:
    def add(self,a,b):
        return a+b+1

base = Base()
derived = Derived()
print(base.add(3,4))
print(derived.add(3,4))


# Funtion Overloading
def Addition(*args):
    print(len(args))
    print(*args)
    print(args)
    return sum(args)

print(Addition(3,4))
print(Addition(3,4,5,6))
'''

