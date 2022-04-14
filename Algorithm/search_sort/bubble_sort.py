def bubble_sort(input_arr: list) -> list:
    result = input_arr[:]
    for j in range(len(result)):
        for i in range(len(result) - 1 -j):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]

    return result

list_ = [12, 2, 4, 5, 18, 19, -1]
print(bubble_sort(list_))
# #### call by refrence or by value

# j = [12, 13]
# print(j)
# def a(input_arr):
#     input_arr[0] = input_arr[1]

# a(j)
# print(j)
