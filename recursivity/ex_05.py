"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   O hiperfatorial de um número N, escrito H(n), é definido por:                       *
*       H(n) = 1¹ * 2² * 3³ * ... * (n -1)^(n-1) * n^n                                  *
*   Sendo assim, faça uma função recursiva que receba um número inteiro positivo N e    *
*   retorne o hiperfatorial desse número.                                               *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def hyperfactorial(n):
    if n >= 1:
        return n**2 * hyperfactorial(n - 1)
    return 1


print(hyperfactorial(8))
