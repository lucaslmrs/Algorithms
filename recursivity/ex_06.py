"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Considere um sistema numérico que não tenha a operação de adição                  *
*   implementada e que você disponha somente dos operadores (funções) sucessor e      *
*   predecessor. Então, pede-se para escrever uma função recursiva que calcule a soma *
*   de dois números x e y através desses dois operadores: sucessor e predecessor.     *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def recursive_sum(value1, value2):
    def successor(n):
        return n + 1

    def predecessor(n):
        return n - 1

    if value2 < 0:
        return recursive_sum(predecessor(value1), successor(value2))
    elif value2 > 0:
        return recursive_sum(successor(value1), predecessor(value2))
    return value1


print(recursive_sum(10, 20))
print(recursive_sum(10, -15))
print(recursive_sum(25, -80))
print(recursive_sum(-15, -20))
print(recursive_sum(-15, 15))