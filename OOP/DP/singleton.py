class SingletonMeta(type):
    _instance = {}

    def __call__(self, *args, **kwds):
        if self not in SingletonMeta._instance:
            SingletonMeta._instance[self] = super().__call__(*args, **kwds)
        print(SingletonMeta._instance)
        return SingletonMeta._instance[self]


class DBInterface(metaclass=SingletonMeta):
    pass


class Logger(metaclass=SingletonMeta):
    pass

obj1 = Logger()
obj2 = Logger()
obj3 = DBInterface()
obj4 = DBInterface()

print(obj1 is obj2)
print(obj1 is obj3)
print(obj4 is obj3)