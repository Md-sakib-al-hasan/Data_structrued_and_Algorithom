# node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# linkList class
class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    # append the single node
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


    # print all linklist
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    # pop the linklist
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


# test
my_link_list = LinkList(1)

my_link_list.append(2)

my_link_list.print_list()
print("append operation is done")

my_link_list.pop()

my_link_list.print_list() 
