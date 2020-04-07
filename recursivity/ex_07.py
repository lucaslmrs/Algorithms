"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Desenvolva um método que seja capaz de converter um número de 16 dígitos            *
*   unsigned (sem sinal) de uma dada base x para outra y. Para isso, efetue os          *
*   seguintes passos básicos:                                                           *
*                                                                                       *
*   1. Converter o número da base de entrada x para a base 10 e, por fim,               *
*      converte-lo para a base y;                                                       *
*   2. Certifique-se de que ambas as bases x e y estão definidas no                     *
*      intervalo [2, 16].                                                               *
*   3. Para dígitos maiores que ‘9’, crie um método que converta seus                   *
*      sucessores nas letras [A,B,C,D,E,F]. Com ‘A’ representando o valor 10 e assim    *
*      por diante.                                                                      *
*                                                                                       *
*   Exemplo: ​public String converterBase( String numero, int x, int y)                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def base_to_base(from_base, to_base, number):

    def base_10_single_converter(num):
        if num.isnumeric():
            num = int(num)
        else:
            if num == 'A': num = 10
            elif num == 'B': num = 11
            elif num == 'C': num = 12
            elif num == 'D': num = 13
            elif num == 'E': num = 14
            elif num == 'F': num = 15
            else:
                print('Please, enter the correct values.')
                exit(-1)
        return int(num)

    def from_base_10_single_converter(num):
        if num == 10: num = 'A'
        elif num == 11: num = 'B'
        elif num == 12: num = 'C'
        elif num == 13: num = 'D'
        elif num == 14: num = 'E'
        elif num == 15: num = 'F'
        return num

    def base_10_converter(base, num='0'):
        current = base_10_single_converter(num[0].upper())

        if current >= base:
            print('Please, enter the correct values.')
            exit(-1)

        if len(num) > 1:
            return current * base**(len(num) - 1) + base_10_converter(base, num[1:])
        else:
            return current

    def from_base_10_converter(base, num=0):
        if num != 0:
            current = from_base_10_single_converter(num % base)
            return f'{from_base_10_converter(base, int(num / base))}' + f'{current}'
        return 0

    def validate_base(base):
        if 2 <= base <= 16:
            return True
        return False

    # function of base-to-base execution
    if validate_base(from_base) and validate_base(to_base):
        return from_base_10_converter(to_base, base_10_converter(from_base, str(number)))
    else:
        print('Please, enter a base between 2 and 16.')


print(base_to_base(16, 2, '16EB34A185'))
