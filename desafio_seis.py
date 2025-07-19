"""
- cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponiveis
- se houver vagas, o aluno deve ser confirmado na turma, e a vaga deve ser reduzida
- se não houver vagas, o aluno deve ser notificado informando que não existem mais vagas
- se um aluno já tiver inscrito em um curso, ele não pode se inscrever novamente
"""

import asyncio

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}
 
alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]

async def processar_inscrição(alunos):
    aluno = alunos['nome']
    curso = alunos['curso']

    print(f"escrevendo o aluno {aluno} no curso {curso}")

    if curso not in cursos:
        print(f"curso não existe na grade curricular")
        return
    curso_nome = cursos[curso]
    if aluno in curso_nome['inscritos']:
        print(f"O aluno já está cadastrado nesta disciplina")
        return
    if curso_nome['vagas'] > 0:
        curso_nome['inscritos'].append(aluno)
        curso_nome['vagas'] -= 1
        print(f"inscrição confirmada para aluno {aluno} no curso {curso}")
    else:
        print(f"Turma Lotada! o aluno {aluno} não conseguiu se inscrever no curso!")

async def main():
    tarefas = [asyncio.create_task(processar_inscrição(a)) for a in alunos]
    await asyncio.gather(*tarefas)
    print("Todas as inscrições foram processadas")

asyncio.run(main())
    
    