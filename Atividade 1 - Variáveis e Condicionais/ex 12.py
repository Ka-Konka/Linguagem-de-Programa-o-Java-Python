import random

def contagem(turmas, alunos):
    lista_alunos = []
    media = alunos // turmas
    print(f'A média de alunos por turma é de {media}')

    for i in range(turmas):
        alunos_turma = random.randint(0, alunos)
        lista_alunos.append(alunos_turma)
        alunos -= alunos_turma

    for i in range(len(lista_alunos)):
        if lista_alunos[i] > 40:
            print(f'A turma {i + 1} tem mais de 40 alunos({lista_alunos[i]}) ')

turmas = int(input('Insira a quantidade de turmas: '))
alunos = int(input('Insira a quantidade de alunos: '))
contagem(turmas, alunos)