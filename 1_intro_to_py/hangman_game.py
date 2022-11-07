import random


def play():
    # Chama mensagem de abertura
    print_opening()

    # Carrega palavra secreta
    secret_word = load_secret_word()

    # Lista com um '_' para cada letra da palavra secreta
    correct_letters = correct_letters_list(secret_word)
    print(correct_letters)

    hanged = False      # flag para enforcado
    got_word = False    # flag para acertou a palavra
    mistakes = 0        # inicializa erros cometidos

    # Enquanto jogador ainda não foi enforcado
    # e nem acertou a palavra...
    while not hanged and not got_word:
        # jogador faz tentativa
        guess = try_guessing()

        if guess in secret_word:
            score_correct_guess(guess, correct_letters, secret_word)
        else:
            mistakes += 1
            draw_hang(mistakes)

        # Se os erros chegarem a 7
        # o jogador é considerado enforcado
        hanged = mistakes == 7

        # Se não existem mais _ na lista
        # todas as letras foram adivinhadas
        # e o jogador venceu o jogo
        got_word = "_" not in correct_letters

        print(correct_letters)

    # Imprime mensagens de acordo com o
    # desempenho do jogador
    if got_word:
        print_winner_msg()
    else:
        print_loser_msg(secret_word)


def print_opening():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def load_secret_word():
    # Esta função sorteia uma palavra secreta
    # a partir de uma lista de palavras
    # armazenadas em um arquivo externo

    # abre o arquivo em modo de leitura (r)
    file = open("words.txt", "r")

    # lista para armazenar as palavras
    words = []

    for line in file:           # Para cada linha do arquivo
        line = line.strip()     # Remove o \n do final da linha
        words.append(line)      # Insere a palavra na lista

    #fecha o arquivo
    file.close()

    # sorteia um número para escolher a palavra secreta
    number = random.randrange(0, len(words))

    # seleciona a palavra secreta, coloca todos as letras em maiúsculo
    # e a retorna
    secret_word = words[number].upper()
    return secret_word


def correct_letters_list(word):
    # Retorna uma lista com um '_' para cada
    # letra da palavra secreta
    return ["_" for letra in word]


def try_guessing():
    # Captura o "chute" do jogador
    guess = input("Qual é a letra? ")

    # Remove espaços (strip) e torna a letra maiúscula (upper)
    # retorna a letra processada
    return guess.strip().upper()


def score_correct_guess(guess, correct_letters, secret_word):
    # Marca o acerto do jogador
    # atualiza as letras da palavra secreta
    index = 0
    for letter in secret_word:
        if guess == letter:
            correct_letters[index] = letter
        index += 1


def draw_hang(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if mistakes == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if mistakes == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if mistakes == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if mistakes == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if mistakes == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if mistakes == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if mistakes == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_winner_msg():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_msg(secret_word):
    print("Você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    play()