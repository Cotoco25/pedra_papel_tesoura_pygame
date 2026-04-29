import random

escolha_ia = ["pedra", "papel", "tesoura"]
adversario = random.choice(escolha_ia)
print(adversario)

choice = input("escolha: ")
if choice == "pedra" and adversario == "papel":
    print("voce ganhou")