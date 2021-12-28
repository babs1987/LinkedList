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
        if len(self)==0:
            self.head=Node(value)
            return
        temp = self.head
        new_node = Node(value)
        while temp.next_ptr is not None:
            temp = temp.next_ptr

        self.len += 1
        temp.set_next_ptr(new_node)

    def pop_last(self):
        if len(self) > 1:
            temp = self.head
            while temp.next_ptr.next_ptr is not None:
                temp = temp.next_ptr
            self.len -= 1
            temp.next_ptr = None
        elif len(self) == 1:
            self.head = None
        else:
            raise KeyError()

    def pop_2_last(self):
        if len(self) > 2:
            self.pop_last()
            self.pop_last()
            self.len -= 2
        elif len(self)==2:
            self.head=None
            self.len=0
        else:
            raise KeyError

    def pop_first(self):
        if len(self) > 0:
            self.head = self.head.next_ptr
            self.len -= 1
        elif len(self)==1:
            self.head=None
        else:
            raise KeyError()

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node
        self.len += 1

    def delete_2_first(self):
        if len(self) > 2:
            self.head = self.head.next_ptr.next_ptr
            self.len -= 2
        elif len(self)==2:
            self.head=None
            self.len=0
        else:
            raise KeyError()

    def del_by_ind(self, index):
        if index == 0:
            self.pop_first()
        elif index == len(self) - 1:
            self.pop_last()
        else:
            temp = self.__getitem__(index - 1)
            temp.next_ptr = self.__getitem__(index + 1)

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)

        elif index == len(self):
            self.append(value)
        else:
            temp = self.__getitem__(index - 1)
            temp.next_ptr = Node(value, temp.next_ptr)
            self.len += 1

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

    def indexy(self, elem):
        index = 0
        if self.head.value == elem:
            return 0
        else:
            temp = self.head
            while temp.next_ptr is not None:
                index += 1
                if temp.next_ptr.value == elem:
                    return index

                temp = temp.next_ptr
        return -1


def Maxy(s):
    if len(s) == 1:
        return s.head.value
    elif len(s) == 0:
        raise KeyError()
    else:
        max = s.head
        temp = s.head
        while temp.next_ptr is not None:
            temp = temp.next_ptr
            if temp.value >= max.value:
                max.value = temp.value

        return max


# 2. Добавить в список L1 за первым вхождением элемента Е все элементы списка L2, вернуть длину нового списка.

def Add_l2_after_e(l1, l2, e):
    tempind = l1.indexy(e)
    if tempind == -1:
        raise KeyError()
    else:
        for i in range(len(l2)):
            # print(f"что {l2.__getitem__(i).value} куда {tempind+1+i}")
            l1.insert(l2.__getitem__(i).value, tempind + i + 1)
        return len(l1)

a = Node(1)
s = LinkedList(a)
s1 = LinkedList(Node(77))
s1.append(88)
s1.append(99)
s1.append(101)
s1.append(1002)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(4)
print("__список l1_________________________")
s.print_list()
print("__список l2_________________________")
s.print_list()
print("____________________________")

print(f"длина нового списка: {Add_l2_after_e(s, s1, 4)}")

s.print_list()

print(f"адрес {Maxy(s)}")
print(f"значение {Maxy(s).value}")

