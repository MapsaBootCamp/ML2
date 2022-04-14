def quick_sort(input_arr: list) -> list:
    if len(input_arr) < 2:
        return input_arr
    pivot = input_arr.pop()

    left = []
    right = []

    for elm in input_arr:
        if elm > pivot:
            right.append(elm)
        else:
            left.append(elm)
    
    left = quick_sort(left)
    right = quick_sort(right)

    result =  left + [pivot] + right

    return result


list_ = [12, 2, 4, 5, 18, 19, -1]
print(quick_sort(list_))



