from src.projetos107 import Aluno
from src.projetos107 import Professor
from src.projetos107 import Aula

professor = Professor("Lucas", 1)
aluno1 = Aluno("Maria", 0)
aluno2 = Aluno("Pedro", 1)
aluno3 = Aluno("Pietro", 1)
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.adicionar_aluno(aluno3)
print(aula.listar_presenca())