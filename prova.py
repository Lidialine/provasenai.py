import random

def main():
    numeroAleatorio = random.randint(0,100)

    tentativas = 5

    print("Tente acertar! ")
    print("Digite um número: ")
    print(f"Você possui {tentativas} chances para acertar.")

    for tentativa in range(1, tentativas +1):
        print(f"\n Tentativa {tentativa} de {tentativas}")

        palpite = int(input("Digite um número entre 1 e 100: "))

        if palpite == numeroAleatorio:
            print("Parabéns, você acertou!")
            break

        elif palpite < numeroAleatorio:
            print("O número secreto é maior!")
    
        else:
            print("O número secreto é menor!")
        
    else:
        print("\n Suas tentativas  acabaram!")
        print(f"O número era {numeroAleatorio}.")
main()