#questão 1
# print("Escreva 3 valores: ");
# x = bool(input());
# y = bool(input());
# z = bool(input());

# if (x and y) or (y and z) or (x and z):
    # print("Pelo menos dois são verdadeiros");
# else: 
    # print("Nenhum ou apenas um é verdadeiro");

# questão 2
# print("Digite um numero:");
# num = int(input());
# for i in range(num):
    # if i % 2 == 0:
        # print(i);

# questão 3
print("Digite um numero:")
num = int(input())

for i in range(2, num):  # Começa do 2, pois 1 não é primo
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):  # Verifica até a raiz quadrada de i
        if i % j == 0:  # Se i for divisível por j, não é primo
            is_prime = False
            break
    if is_prime:
        print("Numero primo:", i)

