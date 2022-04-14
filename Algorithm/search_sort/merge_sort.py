def merge_sort(input_arr: list):
    len_input = len(input_arr)
    if len(input_arr) == 1:
        return input_arr

    middle_index = len(input_arr) // 2

    left = input_arr[:middle_index]
    right = input_arr[middle_index:]

    print("left", left)
    print("right", right)

    left = merge_sort(left)
    right = merge_sort(right)
    
    input_arr = []
    for i in range(len_input):
        if len(left) == 0 or len(right) == 0:
            break
        if left[0] > right[0]:
            input_arr.append(right.pop(0))
        else:
            input_arr.append(left.pop(0))
    
    for elm in left:
        input_arr.append(elm)

    for elm in right:
        input_arr.append(elm)
    
    print("merge sort", input_arr)
    return input_arr



list_ = [12, 2, 4, 5, 18, 19, -1]

print(merge_sort(list_))



# def fibo(idx):
#     if idx == 1 or idx == 2:
#         return 1
#     return fibo(idx-1) + fibo(idx - 2)

# fibo(6)