class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pegar_nome(self):
        return self.name

    def pegar_idade(self):
        return self.age

    def full_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __str__(self):
        return f"Nome: {self.name}, Idade: {self.age}"