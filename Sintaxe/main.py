
first_name = "Kaion";
last_name = "Brandao lima";

print(first_name + " " + last_name);

#Em pyhton não é necessario declarar variavel e nem usar ";", mas em caso de costume, irei continuar usando

number_int = 10;
number_float = 10.5;
name_str = "String teste";
is_bool = True; #Tipo booleano deve ser com letra maiuscula

print(number_int);
print(number_float);
print(name_str);
print(is_bool);

#Trabalhando com string

course_name = "Python programing";
print(len(course_name)); #Retorna o tamanho da String
print(course_name[0]); #Retorna o vetor na posicao [0] de course_name
print(course_name[-1]); #Retorna o vetor na posicao [-1] de course_name sendo a ultima posicao do vetor
print(course_name[0:3]); #Imprime o vetor até determinada posicao
print(course_name[3:]);

#Diferentes caracteres em python

full_name = "Pyhton \"programing\""; #imprimir frase com " "
print(full_name);
print();

#Concatenação

second_name = "Kaion";
thrind_name = "Brandao lima";
mesclagem_name = second_name + " " + thrind_name;
print(mesclagem_name); #Concatendo Strings

mesclagem_name2 = f"{second_name} {thrind_name}"; #Seguna forma de concatenação em python
print(mesclagem_name2);
print();

#Metodos usados em String

course_name_two = "Python programming";
course_name_three = "    Python programming";

modifield_str = course_name_two.upper(); #Modificando variavel para utilizar em outras aplicações
print(course_name_two.casefold());
print(modifield_str);

print(course_name_two.title()); #Inicia toda palavra com letra maiuscula
print(course_name_two.strip()); #Remove espaços em branco de cada lado
print(course_name_three);
print(course_name_three.lstrip()); #Remove espacços em branco apenas do lado esquerdo
print(course_name_three.rstrip()); #Remove espaços apenas do lado direito
print(course_name_two.find("p")); #Retorna o indice da primeira ocorrencia
print(course_name_two.replace("Python", "Django")); #Substitui o termo selecionado
print("Pyt" in course_name_two); #Retorna True ou False




