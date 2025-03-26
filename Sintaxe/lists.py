# lista são mutáveis

my_list = [1, 2, 3, 4, 5];

# print(my_list[0]);
# print(my_list[1]);
# print(my_list[2]);

# print("--------------------")

# print(my_list[-1]);
# print(my_list[-2]);
# print(my_list[-3]);

# print("--------------------")

# print(my_list[0:3]);
# print(my_list[1:4]);

my_list.append(6); #Adiciona elemento ao final da lista
print(my_list);

my_list.insert(3, 33); #Adiciona elemento na posição 3
print(my_list);

my_list.remove(3); #Remove o elemento 3
print(my_list);

my_list.reverse(); #Inverte a lista
print(my_list);

my_list.sort(); #Ordena a lista
print(my_list);

my_list.extend([7, 8, 9]); #Adiciona elementos ao final da lista
print(my_list);

print(my_list.count(7)); #Conta quantas vezes o elemento 7 aparece na lista

print(my_list.index(4)); #Retorna a posicao do elemento 4

my_list.clear(); #Limpa a lista
print(my_list);