"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Implemente uma lista encadeada circular que modela um TAD. Para essa                    *
*   questão, desenvolva os seguintes métodos:                                               *
*                                                                                           *
*   a) Recebe duas listas e verifica se a sequência de dados da segunda lista está          *
*      contida na primeira. Caso esteja, remova a sequência de valores da primeira          *
*      lista.                                                                               *
*   Exemplos:                                                                               *
*   lista1: 2, 5, 7, 10, 1                      Saída: false                                *
*   lista2: 10, 2, 5                                                                        *
*                                                                                           *
*   lista1: 9, 8, 5, 10, 12, 13                 Saída: true                                 *
*   lista2: 10, 12, 13                          Nova lista1: 9, 8, 5                        *
*                                                                                           *
*   lista1: a, b, c, d, e                       Saída: true                                 *
*   lista2: d, e, a                             Nova lista1: b, c                           *
*                                                                                           *
*   b) Dada duas listas L1 e L2, adicionar intercaladamente seus elementos em               *
*      uma outra lista L3;                                                                  *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
from list.tad_lista.linked_list import LinkedList


class LinkedListBuffed(LinkedList):
    def __init__(self):
        super().__init__()
        self.circulate()

    def circulate(self):
        if self._head is not None:
            pointer = self._head
            for i in range(len(self)):
                if i != len(self) - 1:
                    pointer = pointer.next
                else:
                    pointer.next = self._head
                    return

    def insert(self, index, item):
        super().insert(index, item)
        self.circulate()

    def append(self, item):
        super().append(item)
        self.circulate()

    def remove(self, item):
        super().remove(item)
        self.circulate()

    @staticmethod
    def remove_sequence(list1: LinkedList, list2: LinkedList):
        # if the sequence occurs start at the first of the list
        if list1._head is None:
            return False
        elif list2._head is None:
            return False
        elif list1._head.data == list2._head.data:
            pointer_list1 = list1._head
            avaliation = False
            for j, item_list2 in enumerate(list2):
                avaliation = pointer_list1.data == item_list2
                pointer_list1 = pointer_list1.next
                if (not avaliation) or (j == len(list2) - 1):
                    break

            if avaliation:
                list1._head = pointer_list1
                list1._size -= len(list2)
                return True
        else:
            for i, item_list1 in enumerate(list1.node_iterator()):
                item_list1_next = item_list1.next
                avaliation = False
                if item_list1_next.data == list2._head.data:
                    pointer_list1 = list1._getnode(i + 1)
                    for j, item_list2 in enumerate(list2):
                        avaliation = pointer_list1.data == item_list2
                        pointer_list1 = pointer_list1.next
                        if (not avaliation) or (j == len(list2) - 1):
                            break
                if avaliation:
                    item_list1.next = pointer_list1
                    list1._size -= len(list2)
                    return True
            return False

    @staticmethod
    def interlayer(list1: LinkedList, list2: LinkedList):
        if list1._head is None:
            return list2
        if list2._head is None:
            return list1

        list3 = LinkedListBuffed()
        pointer_list1 = list1._head
        pointer_list2 = list2._head

        for item in list1:
            list3.append(pointer_list1.data)
            list3.append(pointer_list2.data)
            pointer_list1 = pointer_list1.next
            pointer_list2 = pointer_list2.next

            if pointer_list1 == list1._head:
                while pointer_list2 != list2._head:
                    list3.append(pointer_list2.data)
                    pointer_list2 = pointer_list2.next
                return list3

            if pointer_list2 == list2._head:
                while pointer_list1 != list1._head:
                    list3.append(pointer_list1.data)
                    pointer_list1 = pointer_list1.next
                return list3
        return list3


if __name__ == '__main__':
    lst1 = LinkedListBuffed()
    lst2 = LinkedListBuffed()
    lst = LinkedListBuffed()

    lst1.append(1)
    lst1.append(2)
    lst1.append(3)
    lst1.append(4)
    lst1.append(5)
    lst1.append(6)
    print('adding in list1', lst1)

    lst2.append(2)
    lst2.append(3)
    lst2.append(4)
    print('adding in list2', lst2)

    print()

    print('interlayer 1 to 2', lst.interlayer(lst1, lst2))
    print('interlayer 2 to 1', lst.interlayer(lst2, lst1))

    print()

    print(lst1)
    print('remove sequence', lst.remove_sequence(lst1, lst2))
    print('list1', lst1)
    print('list2', lst2)
