"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Crie um método recursivo que verifica se todas as letras presentes em uma       *
*   primeira String também estão contidas na segunda.                               *
*   Exemplos:                                                                       *
*       Entrada: “oi” e “abacaxi” → Saída: false                                    *
*       Entrada: “lua” e “australia” → Saída: true                                  *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


def char_contains(char, string):
    if char == string[0] or char == '':
        return True
    elif len(string) > 1:
        return char_contains(char, string[1:])
    else:
        return False

def str_contains(is_contained, main_string):
    try:
        if char_contains(is_contained[0], main_string):
            if len(is_contained) > 1:
                return str_contains(is_contained[1:], main_string)
            return True
        return False
    except IndexError:
        return True


print(str_contains('oi', 'abacaxi'))
print(str_contains('lua', 'australia'))
print(str_contains('ola', 'larissa'))
print(str_contains('', 'wtf'))
