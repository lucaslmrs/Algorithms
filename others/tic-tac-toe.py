def new_board():
    return [[' ' for n in range(0, 3)] for n in range(0, 3)]


def play():
    global counter
    x, y = escolher_posicao()
    make_move(x, y)
    if not iswin(move, x, y):
        if is_draw():
            print_board()
            print('INFELIZMENTE HOUVE UM EMPATE\nTENTEM NOVAMENTE MAIS TARDE')
            play_again()
            return
        counter += 1
        [print() for n in range(0, 5)]
        change_move()
        play()
    else:
        print_board()
        print(f'PARABÉNS!!!\nO  JOGADOR {move} VENCEU.')
        play_again()
        return


def play_again():
    continuar = input('Deseja jogar novamente?? [S/N]: ').upper().startswith('S')
    if continuar:
        zerar()
        play()


def zerar():
    global counter
    global board
    global move
    board = [[' ' for n in range(0, 3)] for n in range(0, 3)]
    move = 'X'
    counter = 1


def escolher_posicao():
    print(f'Jogador "{move}" rodada {counter}')
    print_board()
    while True:
        x = leia_int('Linha: ')
        y = leia_int('Coluna: ')
        if board[x][y] == ' ':
            break
        print('\033[0;31mA CASA ESCOLHIDA JA FOI JOGADA\033[m')
    return x, y


def make_move(x, y):
    global board
    board[x][y] = move


def change_move():
    global move
    if move == 'X':
        move = 'O'
    elif move == 'O':
        move = 'X'


def iswin(jogada, x, y):
    if verif_diagonais(jogada) or verif_linha(jogada, x, y):
        return True
    return False


def verif_diagonais(jogada):
    global board
    if board[0][0] == board[1][1] == board[2][2] == jogada:
        return True
    if board[0][2] == board[1][1] == board[2][0] == jogada:
        return True
    else:
        return False


def verif_linha(jogada, x, y):
    global board
    if board[x][0] == board[x][1] == board[x][2] == jogada:
        return True
    if board[0][y] == board[1][y] == board[2][y] == jogada:
        return True
    else:
        return False


def leia_int(msg):
    try:
        num = int(input(msg)) - 1
        if num not in range(0, 3):
            print('\033[0;31mTivemos um problema com o número que você digitou.\033[m')
            return leia_int('\033[0;31mPor favor, digite um número entre 1 e 3:\033[m ')
    except (ValueError, TypeError):
        print('\033[0;31mTivemos um problema com o tipo que você digitou.\033[m')
        return leia_int('\033[0;31mPor favor, digite um número válido:\033[m ')
    except KeyboardInterrupt:
        print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
        return 0
    else:
        return num


def print_board():
    print('    1\t\t 2\t\t  3')
    for i in range(0, 3):
        print(i + 1, end='  ')
        print(f'({board[i][0]})\t\t({board[i][1]})\t\t ({board[i][2]})')
        print()


def is_draw():
    return counter == 9


board = new_board()
move = 'X'
counter = 1

play()
