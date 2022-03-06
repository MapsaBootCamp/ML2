#OOP Encapsulation, Inheritance, Abstraction, Polymorphism

# class attribute, object attribute
# decorator ----> @
# object method, static method, class method



class ShalghamException(Exception):
    pass


class User:
    count = 0
    
    def __init__(self, username, password) -> None:
        self.username = User._is_string(username)
        self.password = password   # ahmaghane
        self.phone = None
        self.addresses = []

    def get_name(self):
        return self.username

    @classmethod
    def set_address(self, address):
        tmaddress = self._is_string(address)
        self.addresses.append(tmaddress)
    
    @staticmethod
    def _is_string(input_string):
        if isinstance(input_string, str):
            return input_string
        else:
            raise ShalghamException("address should be string")

    @staticmethod
    def _is_phone_number(input_number): # regex
        pass
    

if __name__ == "__main__":
    try:
        user_object = User(True, "1234")
        print(user_object.get_name())  # -----> get_name(user_object)
        user_object.addresses("tehran - sheikh bahai")
        
        user_object_2 = User("asghar", "1234")
    except ShalghamException as error:
        print("error: ", error)