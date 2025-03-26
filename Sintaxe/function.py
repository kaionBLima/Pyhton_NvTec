#Trabalhando com funções em Python

def my_function():
    print("Hello from a function");

my_function();

#função com parametro 
print("--------------------");

def my_function_with_param(param1, param2):
    print(param1 + param2);

my_function_with_param(10, 20);

#função com retorno
print("--------------------");

def my_function_with_return(param1, param2):
    return param1 + param2;

texto = my_function_with_return("Hello", "World");
print(texto);




