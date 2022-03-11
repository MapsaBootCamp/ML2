# with open("test.txt",'a',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")
#    f.write("delemun shirini mikhad\n")

from itertools import count


f = open("test.txt", "w")
# count = 1
# for line in f:
#     print(count, line, end="")
#     count += 1

# a = f.readline()
# print("seek: ", f.tell())
# while a:
#     print(a)
#     a = f.readline()

# for line in f.readlines():
#     print(line)

a = ["Ashkan\t", "az\t", "shoma\t", "kahahesh\t", "mikone", "dars", "dars", "va dars", "bekhunid"]
# import csv

# class Csv:
#     def __init__(self, path="", sep="", header=True):
#         self.data = Csv.create_data(path, sep)
        
#     def get_data(self):
#         return self.data

#     @staticmethod
#     def create_data(path, sep):
#         with open(path, encoding="utf-8") as f:
#             pass

#     def __str__(self):
#         pass

f.writelines(a)

# class ShalghamBasic:
#     count = 0

# class Shalgham(ShalghamBasic):
#     pass


def shalgham_generator(num):
    class ShalghamBasic:
        count = 0

    if num > 10:
        ShalghamBasic.count += 1

    return ShalghamBasic


Shalgham = shalgham_generator(12)
ShalghamGorosneh = shalgham_generator(5)
ShalghamGerun = shalgham_generator(35)


a_obj = Shalgham()
a_obj_gorosne = ShalghamGorosneh()

print(a_obj.count)
print(a_obj_gorosne.count)

class A:
    _count = 10
    class B:
        def __init__(self, name) -> None:
            self.name = name

        def salam(self):
            print("salam", self.name)
    
    def salam(self, mentor="ashkan"):
        print(A._count)
        b = A.B(mentor)
        if mentor == "ashkan":
            b.salam()
        else:
            print("faghat ashkan")


class Field:
    def __init__(self, field) -> None:
        self.field = field


class Table:
    name = Field("name")
    age = Field("age")
    password = Field("password")
    
    class Config:
        table_name = "karbaran"


a = A()
A.B()
a.salam("asghar")