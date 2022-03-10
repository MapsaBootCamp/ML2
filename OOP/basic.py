# class type ----> metaclass(sazande khune) default hame class ha
# class object ----> baba defaukt hame class ha

# class B:
#     def salam_b(self):
#         print("salam in b")

# class C(B):
#     pass

# class D(C):
#     pass

# print("D is subclass of B", issubclass(D, B))
# a = D()
# a.salam_b()

class AMetaClass(type):

    def __call__(self, *args, **kwds):
        print("in __call__ metaclass")
        return super().__call__(*args, **kwds)

    def shab_bekheir(self):
        print("shab bekheir")

class A(metaclass=AMetaClass):
    count = 0

    def __init__(self, name) -> None:
        print("in __init__ class")
        self.name = name

    def __call__(self):
        print("man object class A hastam")
    
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        return super().__new__(cls)

    def salam(self):
        pass
    
    @classmethod
    def my_classmethod(cls):
        cls.count += 1

class B(A):
    pass

# print("B is instance AMetaClass", isinstance(B, type))

# print("object is subclass type: ", issubclass(object, type))
# print("type is subclass object: ", issubclass(type, object))
# print("object is instamce type: ", isinstance(type, object))
# print("type is instamce object: ", isinstance(object, type))


# obj1 = A("Ashkan")
# A.shab_bekheir()
# obj1()
# print(obj1.count)
# obj2 = A("Karim")
# obj2.my_classmethod()
# print(obj1.count)
# obj2.count += 1
# print(obj2.count)

# def a(self):
#     print("man a hastam")

# A.a = a
# obj2.a()


class First:
    def __init__(self):
        print("first")

    def salam_first(self):
        print("salan in first")

class Second(First):
    def __init__(self):
        print("second")

    def salam(self):
        print("salam in second")
    
    def salam_first(self): 
        print("dar Second")
        return super().salam_first()

class Third(First):
    def __init__(self):
        print("third")

    def salam(self):
        print("salam in Third")

class Fourth(Third, Second):
    def __init__(self):
        super().__init__()
        print("that's it")

    def salam(self):
        Third.salam()

# a = Second()
# a.salam_first()

from abc import ABCMeta, abstractclassmethod

# abstrcat class ----> 
# avalan hadaghal yek method abstract darad, 
# dovoman az abstract class hich objecti nemishe sakht, 
# sevoman faghat mitunim ers bari konim va hatman tu bacheha abstract mthod ro piadesazi konim

class User(metaclass=ABCMeta):

    def __init__(self, username) -> None:
        self.username = username
    
    @abstractclassmethod
    def login(self):
        pass

    def salam(self):
        print(f"salam {self.username}")

class Admin(User):
    def login(self):
        print("welcome admin")


class Customer(User):
    def login(self):
        print("welcome admin")




user = Admin("admin")
user.salam()

