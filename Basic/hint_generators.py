my_arr = [3, 4, 5, 2, 56, 76, 5, 4, 3, 44, 3, 2, 222, 1, 22, 44]


class CustomGenrator:

    def __init__(self, arr_) -> None:
        self.arr_ = arr_

    def __iter__(self):
        print("salam")
        cursor = 0

        if len(self.arr_) < 4:
            return self.arr_

        while cursor < len(self.arr_):
            if len(self.arr_) - cursor < 3:
                return self.arr_[cursor:]
            yield self.arr_[cursor: cursor + 3]
            cursor += 3


# def custom_genrator(arr_):
#     print("salam")
#     cursor = 0

#     if len(arr_) < 4:
#         return arr_

#     while cursor < len(arr_):
#         if len(arr_) - cursor < 3:
#             return arr_[cursor:]
#         yield arr_[cursor: cursor + 3]
#         cursor += 3


a = CustomGenrator(my_arr)
for elm in a:
    print(elm)

for elm in a:
    print(elm)