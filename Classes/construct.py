class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome} \nIdade: {self.idade}"
    
    def display_info(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")

class Student(Person):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def __str__(self):
        return f"{super().__str__()} \nMatrícula: {self.matricula}"


p = Person("Kaion", 20)
print(p)
s = Student("João", 20, 123)
s.display_info(); 
