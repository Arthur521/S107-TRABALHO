class Aula:
    def __init__(self, professor, assunto):
        if not isinstance(assunto, str):
            raise TypeError("O assunto da aula deve ser um texto (str).")
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno is None:
            raise ValueError("Nenhum aluno foi fornecido para adicionar.")
        if not hasattr(aluno, 'nome'):
            raise AttributeError("O objeto fornecido não possui o atributo 'nome'.")
        if not hasattr(aluno, 'genero'):
            raise AttributeError("O objeto fornecido não possui o atributo 'genero'.")
        if aluno.nome is None:
            raise TypeError("O nome do aluno não pode ser None.")
        if aluno.genero is None:
            raise AttributeError("O gênero do aluno não pode ser None.")
        self.alunos.append(aluno)

    def listar_presenca(self):
        if not self.alunos:
            raise ValueError("Nenhum aluno foi adicionado à aula. A lista de presença está vazia.")
        if not hasattr(self.professor, 'ministrar_aula'):
            raise AttributeError("O professor fornecido não possui o método 'ministrar_aula'.")
        self.professor.ministrar_aula(self.assunto)
        for aluno in self.alunos:
            if not hasattr(aluno, 'presenca'):
                raise AttributeError("Um dos alunos não possui o método 'presenca'.")
            aluno.presenca()
