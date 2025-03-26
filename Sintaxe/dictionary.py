# Trabalhandondo com dicionários temos apenas chave e valor, não temos índices.

my_dict = {"nome": "João", "idade": 25, "cidade": "São Paulo"};
print(my_dict["nome"]);
print(my_dict.get("idade"));
print(my_dict.keys()); #Retorna as chaves
print(my_dict.values()); #Retorna os valores das chaves
print(my_dict.items()); #Retorna as chaves e os valores
my_dict["idade"]: 30; #Altera o valor da chave idade
my_dict["País"] = "Brasil"; #Adiciona a chave País
print(my_dict);
my_dict.pop("cidade"); #Remove a chave cidade
print(my_dict);