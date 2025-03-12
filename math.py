import math;

print(round(2.9))  # arredondar numero
print(math.pi)
print(abs(-2.9))
print(pow(2, 3))  # potenciação
print(max(2, 3))  # numero maximo/maior
print(min(2, 3))  # numero minimo/menor
print(sum([1, 3, 5]))  # soma
print(chr(65))  # Retorna valor da tabela ASCII
print(ord('A'))  # Retorna valor da tabela ASCII
print(divmod(10, 3))  # retorna o resto da divisão
print(math.ceil(2.1))
print(math.floor(2.9))

print("-----------------------------------")

x = input('Digite um número: ')
print(type(x))  # Aqui, 'x' será do tipo 'str'

y = int(x) + 1  # Convertendo x para inteiro antes de somar
print(y)

print("------------------------------------")

print(2 > 1);
print(2 <= 1);
print(2 >= 1);
print(2 < 1);
print(2 == 1);

print("------------------------------------")

meaning = 30;

if meaning > 10:
    print('Right on!');
else: 
    print('No today');

print('All done');

print("------------------------------------")

#Operador ternario
meaning = 30;
print("Righ on!") if meaning > 10 else print("Not today");