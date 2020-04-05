"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Dado um número natural n na base decimal, escreva um método recursivo que        *
*   retorna seu valor na base binária.                                               *
*   Exemplos:                                                                        *
*   print(retornaBinario(4))                                                         *
*   Saída: 100                                                                       *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def binary(num=0):
    if num != 0:
        return f'{binary(int(num / 2))}' + f'{num % 2}'
    return str(num)


print(binary(25))
