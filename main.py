class Node:
    def __init__(self, value, next_ptr=None):
        self.value = value
        self.next_ptr = next_ptr

    def set_value(self, value):
        self.value = value

    def set_next_ptr(self, next_ptr):
        self.next_ptr = next_ptr


class LinkedList:
    def __init__(self, head):
        self.head = head
        if self.head is not None:
            self.len = 1
        else:
            self.len = 0

    def __len__(self):
        return self.len

    def append(self, value):
        temp = self.head
        new_node = Node(value)
        while temp.next_ptr is not None:
            temp = temp.next_ptr

        self.len += 1
        temp.set_next_ptr(new_node)

    def pop_last(self):
        temp = self.head
        while temp.next_ptr.next_ptr is not None:
            temp = temp.next_ptr

        self.len -= 1
        temp.next_ptr = None

    def pop_first(self):
        self.head = self.head.next_ptr
        self.len -= 1

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node
        self.len += 1

    def del_by_ind(self, index):
        if index == 0:
            self.pop_first()
        elif index == len(self) - 1:
            self.pop_last()
        else:
            temp = self.__getitem__(index - 1)
            temp.next_ptr = self.__getitem__(index + 1)

    def insert(self,value,index):
        if index==0:
            self.prepend(value)
        elif index==len(self)-1:
            self.append(value)
        else:
            temp=self.__getitem__(index-1)
            temp.next_ptr=Node(value,temp.next_ptr)

    def __getitem__(self, index):
        i = 0
        temp = self.head
        while i < index and temp.next_ptr is not None:
            temp = temp.next_ptr
            i += 1

        if i == index:
            return temp
        else:
            raise KeyError()

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next_ptr
