import re


def remove_chars(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def get_one_digit(cnpj, list_validate):
    result = list()
    for pos, n in enumerate(cnpj):
        result.append(int(n) * int(list_validate[pos]))

    digit = 11 - (sum(result) % 11)
    return digit if digit <= 9 else 0


def first_digit(cnpj):
    list_validate = '543298765432'
    return str(get_one_digit(cnpj, list_validate))


def second_digit(cnpj):
    list_validate = '6543298765432'
    return str(get_one_digit(cnpj, list_validate))


def get_digits(cnpj):
    cnpj = cnpj[0:-2]
    cnpj = cnpj + first_digit(cnpj)
    return cnpj + second_digit(cnpj)


def is_sequence(cnpj):
    return cnpj[0]*len(cnpj) == cnpj


#   main function
def cnpj_is_valid(cnpj):
    cnpj = remove_chars(cnpj)
    if is_sequence(cnpj):
        return False
    new_cnpj = get_digits(cnpj)
    return cnpj == new_cnpj


print(cnpj_is_valid('12.544.992/0001-05'))
