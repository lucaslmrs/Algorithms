"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Utilizando a recursividade, escreva métodos recursivos capazes de fazer as      *
*   seguintes operações (utilize métodos auxiliares, se necessário):                *
*                                                                                   *
*   a) Somar todos os números primos de um intervalo fechado de números;            *
*                                                                                   *
*   b) Multiplicar todos os elementos pares para a n-ésima sequência de Fibonacci.  *
*   Exemplo: public int multiFib(int n);                                            *
*                                                                                   *
*   Entrada         Saída                                                           *
*    n = 1            0                                                             *
*    n = 4            2                                                             *
*    n = 7           16                                                             *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def question_a():
    def is_prime(target, current=2):
        if target == current:
            return True
        elif target % current == 0:
            return False
        else:
            return is_prime(target, current + 1)

    def calculate(current, end, result=0):
        if current <= end:
            result += (current if is_prime(current) else 0)
            return calculate(current + 1, end, result)
        return result

    def prime_sum(start, end):
        start = 2 if start < 2 else start
        return calculate(start, end)

    print(prime_sum(5, 29))


def question_b():
    def fibonacci(target, sequence=[0, 1]):
        length = len(sequence)
        if length < target:
            sequence.append(sequence[length - 1] + sequence[length - 2])
            return fibonacci(target, sequence)
        return sequence

    def even_multiplication_fibonacci(sequence, result=0):
        if len(sequence) > 1:
            current = sequence.pop()
            is_par = current % 2 == 0
            if is_par:
                result *= current
                if result == 0:
                    result = current
            return even_multiplication_fibonacci(sequence, result)
        return result

    fib = fibonacci(7)
    print(fib)
    print(even_multiplication_fibonacci(fib))


question_a()
question_b()
