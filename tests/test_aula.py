import pytest

from src import Aluno
from src import Professor
from src import Aula

def test_criar_aula_com_assunto_valido():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    assert aula.assunto == "Matemática"

def test_adicionar_aluno():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    aluno = Aluno("Ana", 0)
    aula.adicionar_aluno(aluno)
    assert aluno in aula.alunos

def test_presenca_aluno(capfd):
    aluno = Aluno("Ana", 0)
    aluno.presenca()
    captured = capfd.readouterr()

    # Verifica se a saída contém o texto esperado
    assert captured.out == "A aluna Ana está presente\n"

def test_listar_presenca(capfd):
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    aluno1 = Aluno("Ana", 0)
    aluno2 = Aluno("João", 1)
    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    aula.listar_presenca()
    captured = capfd.readouterr()
    assert captured.out == "O professor Carlos está ministrando uma aula sobre Matemática\nA aluna Ana está presente\nO aluno João está presente\n"

def test_criar_aula_com_assunto_como_string():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    assert isinstance(aula.assunto, str)

# Testes negativos
def test_criar_aula_com_assunto_invalido():
    professor = Professor("Carlos", 1)
    with pytest.raises(TypeError):
        Aula(professor, 123)  # Assunto não é string

def test_adicionar_aluno_sem_nome():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    aluno = Aluno(None, 0)
    with pytest.raises(TypeError):
        aula.adicionar_aluno(aluno)

def test_adicionar_aluno_sem_genero():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    aluno = Aluno("Ana", None)
    with pytest.raises(AttributeError):
        aula.adicionar_aluno(aluno)

def test_adicionar_aluno_none():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    with pytest.raises(ValueError):
        aula.adicionar_aluno(None)

def test_listar_presenca_com_aula_vazia():
    professor = Professor("Carlos", 1)
    aula = Aula(professor, "Matemática")
    with pytest.raises(ValueError):
        aula.listar_presenca()