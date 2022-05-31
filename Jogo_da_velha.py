from colorama import Fore, init  # Para personalizar as cores
from os import system

init(autoreset=True)  # Reseta as cores automaticamente

def limpa():  # Limpa o terminal
    system('cls')

def gera_tabuleiro():  # Tabuleiro a ser alterado
    tabuleiro = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
    return tabuleiro

def print_tabuleiro(tabuleiro):  # Tabuleiro visualizável
    print(' ', tabuleiro[0][0], ' | ', tabuleiro[0][1], ' | ', tabuleiro[0][2])
    print('-'*17)
    print(' ', tabuleiro[1][0], ' | ', tabuleiro[1][1], ' | ', tabuleiro[1][2])
    print('-'*17)
    print(' ', tabuleiro[2][0], ' | ', tabuleiro[2][1], ' | ', tabuleiro[2][2])

def verifica_jogada(tabuleiro, linha, coluna):  # Verifica se o campo a ser preenchido está vazio
    if tabuleiro[linha-1][coluna-1] == ' ':
        return True
    else:
        return False

def verifica_resultado(tabuleiro):  # Verifica se há um vencedor, se "deu velha" ou se o jogo deve prosseguir
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[0][0]} Venceu!')
        return True
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][2] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[1][0]} Venceu!')
        return True
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][2] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[2][0]} Venceu!')
        return True
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[2][0] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[0][0]} Venceu!')
        return True
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[2][1] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[0][1]} Venceu!')
        return True
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and tabuleiro[2][2] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[0][2]} Venceu!')
        return True
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[2][2] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[0][0]} Venceu!')
        return True
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[2][0] != ' ':
        print_tabuleiro(tabuleiro)
        print(Fore.GREEN + f'Jogador {tabuleiro[0][2]} Venceu!')
        return True
    else:
        if not ' ' in tabuleiro[0] and not ' ' in tabuleiro[1] and not ' ' in tabuleiro[2]:
            print_tabuleiro(tabuleiro)
            print(Fore.YELLOW + 'Deu velha!')
            return True
        else:
            return False

def jogar():
    limpa()
    tabuleiro = gera_tabuleiro()
    vez = 1  # Alterna entre 1 (jogador 1) e -1 (jogador 2)
    while not verifica_resultado(tabuleiro):
        if vez == 1:
            while True:
                print_tabuleiro(tabuleiro)
                print('\nJogador 1 - X')
                try:
                    linha = int(input('Digite a linha: '))
                    coluna = int(input('Digite a coluna: '))
                    if not verifica_jogada(tabuleiro, linha, coluna):
                        limpa()
                        print(Fore.RED + 'Campo já preenchido.')
                    else:
                        limpa()
                        tabuleiro[linha-1][coluna-1] = 'X'
                        vez = vez * -1  # Altera o sinal de 1
                        break

                except:
                    limpa()
                    print(Fore.RED + 'Jogada inválida.')
        else:
            while True:
                print_tabuleiro(tabuleiro)
                print('\nJogador 2 - O')
                try:
                    linha = int(input('Digite a linha: '))
                    coluna = int(input('Digite a coluna: '))
                    if not verifica_jogada(tabuleiro, linha, coluna):
                        limpa()
                        print(Fore.RED + 'Jogada inválida')
                    else:
                        limpa()
                        tabuleiro[linha-1][coluna-1] = '0'
                        vez = vez * -1  # Altera o sinal de 1
                        break
                except:
                    limpa()
                    print(Fore.RED + 'Jogada inválida.')

def menu():
    print('-='*17)
    print(f'{"Bem vindo ao jogo da velha":^34}')
    print('-='*17)
    inicio = input('Deseja jogar?'
                       '\n1- Sim'
                       '\n2- Não\n')
    if inicio.lower() in ['sim', '1']:
        jogar()
    elif inicio.lower() in ['não', 'nao', '2']:
        print('Ok, até logo!')
    else:
        limpa()
        print(Fore.RED + 'Não entendi, tente novamente.\n')
        menu()

menu()
input('\nAperte enter para fechar.')