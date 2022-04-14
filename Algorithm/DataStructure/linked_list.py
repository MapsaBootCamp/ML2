class LinkedList:

    class Node:
        def __init__(self, data=None) -> None:
            self.data = data
            self.next: LinkedList.Node = None

    def __init__(self) -> None:
        self.root: LinkedList.Node = None

    def add_begin(self, data):
        node = LinkedList.Node(data)
        if not self.root:
            self.root = node
        else:
            node.next = self.root
            self.root = node

    def append(self, data):
        node = LinkedList.Node(data)
        if not self.root:
            self.root = node
        else:
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = node
            
    def pop(self):
        if not self.root:
            raise Exception("empty linked list")
        elif not self.root.next:
            result = self.root.data
            self.root = None
            return result
        else:
            temp = self.root
            while temp.next.next:
                temp = temp.next
            result = temp.next.data
            temp.next = None
            return result

    def __len__(self):
        pass

    def __str__(self) -> str:
        result = "$$"
        temp = self.root
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += " -> "
        result += "$$"
        return result



l = LinkedList()
l.add_begin("ashkan")
l.add_begin(124)
l.add_begin(["sajhsjhf", 13456])
l.append("mapsa")
print(l)
a = l.pop()
a = l.pop()
a = l.pop()
a = l.pop()

print(l)
print(a)