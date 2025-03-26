class Person:
    nome: "";
    idade: 0;
    email: "";
    curso: "";
    periodo: 0;

    def get_Info(self):
        print(f"Nome: {self.nome} \n Idade: {self.idade} \n Email: {self.email} \n Curso: {self.curso} \n Periodo: {self.periodo}");

p = Person();
p.nome = "Kaion"; 
p.idade = 20;
p.email = "joao@gmail.com";
p.curso = "Engenharia de Software";
p.periodo = 4;

p.get_Info();