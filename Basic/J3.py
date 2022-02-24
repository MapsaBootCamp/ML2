from typing import List, Optional
from functools import reduce

def _a():
    print("aaa")


def _logarithm():
    print("logarithm dar jalase 3")


def test_a():
    print("test a in jalaseh 3")

# def sum(a, b):
#     print(f"a={a}, b={b}, {a} + {b} ={a+b}")
#     return a + b

# print(reduce(sum, [1, 2, 3, 4]))

matrix1  = [
                [3, 2], 
                [6, 13]
            
        ]

matrix2  = [
                [1, 0], 
                [0, 1]
            
        ]

# zip function
# litter = [2, 4]
# jitter = [3, 4, 23]
# gitter = [56, 4]
# for elm in zip(litter, jitter, gitter):
#     print("zip: ", elm)


# tuple_ = (2, 4, 12)
# a, c, f = tuple_
# print(a, c)

# temp = []
# for e in range(10):
#     if e > 3:
#         temp.append(e)

# # Comprehension
# print([e for e in range(10) if e>3])


# for indx, elm in enumerate(matrix_):
#     print(indx, elm)

def matrix_mulyiply(mat1: List[List], mat2: List[List]) -> Optional[List]:
    mat1_row = len(mat1)
    mat1_col = (lambda mat1=mat1: len(mat1[0]) if len(mat1)>0 else 0)()
    mat2_row = len(mat2)
    mat2_col = (lambda mat2=mat2: len(mat2[0]) if len(mat2)>0 else 0)()

    if mat1_col == mat2_row:
        result = [[0 for x in range(mat2_col)] for y in range(mat1_row)]
        for i in range(mat1_row):
            for j in range(mat2_col):
                for k in range(mat2_row):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result
    else:
        raise Exception("zarb pazir nistan")

def matrix_mulyiply2(mat1: List[List], mat2: List[List]) -> Optional[List]:
    mat1_row = len(mat1)
    mat1_col = (lambda mat1=mat1: len(mat1[0]) if len(mat1)>0 else 0)()
    mat2_row = len(mat2)
    mat2_col = (lambda mat2=mat2: len(mat2[0]) if len(mat2)>0 else 0)()

    if mat1_col == mat2_row:
        result = []
        for i in range(mat1_row):
            result_row = []
            for j in range(mat2_col):
                temp =0
                for k in range(mat2_row):
                    temp += mat1[i][k] * mat2[k][j]
                result_row.append(temp)
            result.append(result_row)
        return result
    else:
        raise Exception("zarb pazir nistan")



messi_session_goals = [80, 80, 80, 32, 34, 54, 54]

# tables = [lambda x=x: x*10 for x in range(1, 11)]

# for table in tables:
#     print(table())


a = [-4, 3, -4, 5, 6, 7, -4 , 5]
b = set(a)
temp = []
for elm in b:
    if a.count(elm) > 1:
        temp.append(-elm)


def a(stop, *args):
    if len(args) > 0:
        


if __name__ == "__main__":
    a(13)
    print(temp)
    print(list(map(lambda x, y: (3*x, 4*y), [1, 2, 3, 4], [4, 5, 6])))

    print(matrix_mulyiply2(matrix1, matrix2))

    print("in jalaseh 3: ", __name__)
