import random

def play():
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    secret_number = random.randrange(1, 101)
    points = 1000
    tries = 0

    print("Defina o nível de dificuldade")
    level = int(input("(1)Fácil (2)Médio (3)Difícil\n"))

    if level == 1:
        tries = 20
    elif level == 2:
        tries = 10
    else:
        tries = 5

    for run in range(tries):
        print("\nTentativa {} de {}".format(run+1, tries))
        guess_str = input("Qual o seu chute? (Entre 1 e 100): ")
        guess = int(guess_str)

        correct = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if guess < 1 or guess > 100:
            print("Você deve digitar um número entre 1 e 100!")
            points -= 100
            continue

        if correct:
            print("Acertô miseravi!")
            points += (tries - run) * level
            break
        else:
            if bigger:
                print("Errrrooouuu! O seu chute foi maior que o número secreto.")
            elif smaller:
                print("Errrrooouuu! O seu chute foi menor que o número secreto.")

            points -= abs(secret_number - guess)

    print(f"Pontuação: {points}")
    print("\nFim do Jogo!")

if __name__ == "__main__":
    play()