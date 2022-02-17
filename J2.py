# functions, variables, objects ===> snack case  ashkan_divband
# class ===> pascal case  ==> AshkanDivband

from typing import Tuple, List

my_list = ["ashkan", True, 2, 2.3, ["mapsa"], {"name": "ashkan"}, ("ashgar", 2), {2, 2.6}]

print("address l bar aval: ", id(my_list))
my_tuple1 = ("a", my_list)

print("eleman aval: ", my_tuple1[1])
print("address mytuple1 bar aval: ", id(my_tuple1))

my_list.append("sandogh")


print("address l bar dovom: ", id(my_list))
print("eleman aval: ", my_tuple1[1])
print("address mytuple1 bar dovom: ", id(my_tuple1))


a = [True]
b = [True]

my_tuple2 = "b"
# {[2]: "ashkan"}  #Error


print("my tuple1 address:" ,id(my_tuple1))
print("my tuple2 address: ", id(my_tuple2))

print(a == b)



# function(adad) ---> return list ----> hamegi mazareb 3 az khodesh kuchiktar

def smaller_than_number_mul3(number : int) -> List:
    result = []
   
    # iterable(e.g, string, list, tuple, set, dic, iterable objects)
    for elm in range(1, number):
        if elm%3 == 0:
            result.append(elm)
    return result


def is_prime(number) -> bool:
    if number == 2:
        return True
    for i in range(2, number):
        if not number%i: # pythonic
            return False
    return True

def prime_numbers_smaller_than_input(number: int) -> List:
    result = []

    for i in range(2, number):
        if is_prime(i):
            result.append(i)
    return result


def sample_fun(a, b, c=12, d=14):
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("d: ", d)

def sample_fun_2(a, *args, **kwargs):
    print("positional args: ",args)
    print("default args: ", kwargs)

print(smaller_than_number_mul3(12))  # invoke
print(prime_numbers_smaller_than_input(30))
sample_fun(1, 4, d=7)
sample_fun_2(2, 3, 5, 8, c=6, b=12)



