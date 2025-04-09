class Aluno:
    def __init__(self, nome, genero):
        try:
            self.nome = nome
            if genero not in [0, 1]:
                raise ValueError("Gênero inválido! O gênero deve ser 0 (feminino) ou 1 (masculino).")
            self.genero = genero
        except ValueError as e:
            print(f"Erro: {e}")

    def presenca(self):
        if self.genero == 0:
            print(f'A aluna {self.nome} está presente')
        elif self.genero == 1:
            print(f'O aluno {self.nome} está presente')