class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, Aluno):
        self.alunos.append(Aluno)
        

    def listar_presenca(self):
        print('Presenca da aula sobre ', self.assunto, 'ministrada pelo professor ', self.professor.nome, ':')
        for Aluno in self.alunos:
            Aluno.presenca()


class Professor:
    def __init__(self, nome):
        self.nome = nome
        
    def ministrar_aula(self, assunto):
        print('O professor', self.nome, 'esta ministrando uma aula sobre ', assunto) 


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print('O aluno', self.nome, 'esta presente') 


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()
professor.ministrar_aula("banco de dados nao relacionais")