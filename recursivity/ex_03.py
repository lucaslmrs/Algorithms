"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Considerando um número arbitrário máximo 1000, crie um método recursivo que     *
*   imprime na tela uma sequência de números, primeiro em ordem crescente e depois  *
*   decrescente, inicialmente de um número passado como argumento, e então          *
*   multiplicando-o por 2 sem passar do número máximo.                              *
*   Ex.:                                                                            *
*   public void seq(int n);                                                         *
*   seq(100) = 100, 200, 400, 800, 800, 400, 200, 100                               *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def sequence(start, multiplier=2, end=1000):
    try:
        if start <= end:
            return f'{start}' + f' {sequence(start * multiplier, multiplier, end)} ' + f'{start}'
        return ''
    except RecursionError as error:
        print(f'\033[0;31m\n\nInvalid parameters. Please, try again: {error.__class__}\033[m')
        exit(-1)


print(sequence(100, 2))
