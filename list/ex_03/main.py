"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Utilizando uma lista simplesmente ligada que armazena Strings em seus nós,              *
*   efetue a inversão da lista conforme os exemplos abaixo. Faça a inversão através         *
*   dos campos de ligação, e NÃO dos campos de informação.                                  *
*   Exemplos:                                                                               *
*                                                                                           *
*    Lista original             Lista invertida                                             *
*        1→2→2→3                    3→2→2→1                                                 *
*   d→e→v→e→l→o→p→e→r          r→e→p→o→l→e→v→e→d                                            *
*       Eu→amo→ED                  ED→amo→Eu                                                *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
from list.tad_lista.linked_list import LinkedList


def flip_list(list: LinkedList):
    new_list = LinkedList()
    size = len(list)
    for i in range(1, size + 1):
        new_list.append(list[size - i])
    return new_list


if __name__ == "__main__":
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst)
    print(flip_list(lst))
    print(lst)
