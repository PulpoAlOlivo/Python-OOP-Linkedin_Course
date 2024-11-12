"""
Python Polymorphism example
"""
class ClassA:
    def my_lovely_method(self):
        print('my_lovely_method() from ClassA')
class ClassB(ClassA):
    def my_lovely_method(self):
        print('my_lovely_method() from ClassB')

objectA = ClassA()
objectB = ClassB()
objectA.my_lovely_method()
objectB.my_lovely_method()
        


