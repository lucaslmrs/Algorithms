from list.tad_lista.node import Node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def __str__(self):
        string = 'INICIO --> [ '
        for elem in self:
            string += f' {elem},'
        string = string[0:-1] + '  ]'
        return string

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        try:
            pointer = self.__head
            for i in range(self.__size):
                yield pointer.data
                pointer = pointer.next
        except Exception:
            pass

    def print_list(self):
        print(self)

    def __len__(self):
        return self.__size

    def __getnode(self, index):
        if index < 0:
            if abs(index) > self.__size:
                raise IndexError(f"List index ({index}) out of range")
            index = self.__size + index
        pointer = self.__head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError(f"List index ({index}) out of range")
        return pointer

    def __getitem__(self, index: int):
        pointer = self.__getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError(f"List index ({index}) out of range")

    def __setitem__(self, index: int, item):
        pointer = self.__getnode(index)
        if pointer:
            pointer.data = item
        else:
            raise IndexError(f"List index ({index}) out of range")

    def contains(self, item):
        for elem in self:
            if elem == item:
                return True
        return False

    def index(self, item):
        count = 0
        for elem in self:
            if elem == item:
                return count
            count += 1
        raise ValueError(f"{item} is not in list")

    def empty(self):
        self.__head = None

    def size(self):
        return self.__size

    def append(self, item):
        if self.__head:
            pointer = self.__head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(item)
        else:
            self.__head = Node(item)
        self.__size += 1

    def insert(self, index, item):
        node = Node(item)
        if index == 0:
            node.next = self.__head
            self.__head = node
        else:
            pointer = self.__getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self.__size += 1

    def remove(self, item):
        if self.__head is None:
            raise ValueError(f"{item} is not in list")
        elif self.__head.data == item:
            self.__head = self.__head.next
            self.__size -= 1
            return True
        else:
            pointer = self.__head
            while pointer.next:
                if pointer.next.data == item:
                    pointer.next = pointer.next.next
                    self.__size -= 1
                    return True
                pointer = pointer.next
            raise ValueError(f"{item} is not in list")


if __name__ == '__main__':
    lst = LinkedList()
    lst.append(8)
    lst.append(9)
    lst.append(34)
    lst.append(1)
    lst.append(32)
    lst.append(245)
    lst.append(4567)
    lst.append(356)
    lst.print_list()
    lst[-8] = 5
    lst.insert(2, 10)
    print(lst.contains(10))
    lst.print_list()
    print(lst.remove(10))
    lst.print_list()
    print(lst.index(34))
    print(lst.size())
    lst.empty()
    lst.print_list()
