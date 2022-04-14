def find_single(input_arr):
    
    mid = len(input_arr) // 2
    if len(input_arr) == 1:
        return input_arr[0]
    elif input_arr[mid] != input_arr[mid + 1] and input_arr[mid -1] != input_arr[mid]:
        return input_arr[mid]
    elif mid%2 == 0:
        if input_arr[mid] == input_arr[mid + 1]:
            return find_single(input_arr[mid:])
        else:
            return find_single(input_arr[:mid+1])
    else:
        if input_arr[mid] == input_arr[mid + 1]:
            return find_single(input_arr[:mid])
        else:
            return find_single(input_arr[mid+1:])

list_ = [10, 10, 2, 2, 4, 1, 1, 5, 5, 3, 3]
print(find_single(list_))