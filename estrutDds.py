for i in range(10):
    print(i); #Contador que vai de 0 a 9

print("--------------------");

c = 0;
while c < 10:
    print(c)
    c += 1 #Contador que incrementa de 0 a 9

print("--------------------");

for i in range(10):
    if i == 5: #Parou no 5
        break 
    print(i);

print("--------------------");

for i in range(10):
    if i == 5: #Excluiu o 5 de jogada
        continue
    print(i);

print("--------------------");

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
array_nam = ["joao", "Maria", "Jose", "Ana", "Paula"];


for i in array:
    print(i); #Imprime um array de 1 a 10
print();
for i in array_nam:
    print(i); #Imprime array de nomes

print("--------------------");

x = 10;
y = 20;

if x > 0 and y > 0:
    print("Ambos são positivos");

if x > 0 or y > 0:
    print("Pelo menos um deles é positivo");

if not x > 0:
    print("X não é positivo");

