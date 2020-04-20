from list.tad_lista.node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self):
        string = 'INICIO --> [ '
        for elem in self:
            string += f' {elem},'
        string = string[0:-1] + '  ]'
        return string

    def __repr__(self):
        return self.__str__()

    def __func_iter(self, func):
        try:
            pointer = self._head
            for i in range(self._size):
                yield func(pointer)
                pointer = pointer.next
        except AttributeError:
            pass

    def __iter__(self):
        data_iter = self.__func_iter(lambda node: node.data)
        for item in data_iter:
            yield item

    def node_iterator(self):
        linked_iter = self.__func_iter(lambda node: node)
        for item in linked_iter:
            yield item

    def print_list(self):
        print(self)

    def __len__(self):
        return self._size

    def _getnode(self, index):
        if index < 0:
            if abs(index) > self._size:
                raise IndexError(f"List index ({index}) out of range")
            index = self._size + index
        pointer = self._head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError(f"List index ({index}) out of range")
        return pointer

    def __getitem__(self, index: int):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError(f"List index ({index}) out of range")

    def __setitem__(self, index: int, item):
        pointer = self._getnode(index)
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
        self._head = None

    def size(self):
        return self._size

    def append(self, item):
        if self._head:
            pointer = self._head
            for i in range(len(self) - 1):
                pointer = pointer.next
            pointer.next = Node(item)
        else:
            self._head = Node(item)
        self._size += 1

    def insert(self, index, item):
        node = Node(item)
        if index == 0:
            node.next = self._head
            self._head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, item):
        if self._head is None:
            raise ValueError(f"{item} is not in list")
        elif self._head.data == item:
            self._head = self._head.next
            self._size -= 1
            return True
        else:
            pointer = self._head
            while pointer.next:
                if pointer.next.data == item:
                    pointer.next = pointer.next.next
                    self._size -= 1
                    return True
                pointer = pointer.next
            raise ValueError(f"{item} is not in list")

    def pop(self):
        if self._head is None:
            raise ValueError(f"The list is empty")
        elif self._size == 1:
            current = self._head.data
            self._head = None
            self._size -= 1
            return current
        else:
            pointer = self._head
            while pointer.next.next:
                pointer = pointer.next
            current = pointer.next.data
            pointer.next = None
            self._size -= 1
            return current


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
    print(lst.pop())
    lst.print_list()
    lst.empty()
    print(lst)
