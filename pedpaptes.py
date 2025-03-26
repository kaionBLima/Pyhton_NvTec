import random
print("JOGO DO PEDRA, PAPEL E TESOURA");
print("____________________________")

print("Pedra, papel, tesoura... (escolha uma opção)");


play1 = input("Player 1: ");
mac = None

match play1:

    case "pedra":
        mac = random.choice(["pedra", "papel", "tesoura"]);
    case "papel":
        mac = random.choice(["pedra", "papel", "tesoura"]);
    case "tesoura":
        mac = random.choice(["pedra", "papel", "tesoura"]);

print("Maquina:", mac);
print("--------------------------------")
if play1 == mac:
    print("Empate!");
elif play1 == "pedra" and mac == "tesoura":
    print("Player 1 venceu!");
elif play1 == "papel" and mac == "pedra":
    print("Player 1 venceu!");
elif play1 == "tesoura" and mac == "papel":
    print("Player 1 venceu!");
elif play1 != "pedra" or play1 != "papel" or play1 != "tesoura":
    print("Opção inválida! Tente novamente.");
else:
    print("Maquina venceu!");
