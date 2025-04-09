class Professor:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

    def ministrar_aula(self, assunto):
        if self.genero == 1:
            print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}')
        elif self.genero == 0:
            print(f'A professora {self.nome} está ministrando uma aula sobre {assunto}')
