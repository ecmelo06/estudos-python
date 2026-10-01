"""
Crie um programa em Python que receba as notas finais de vários
alunos, com valores float de 0 a 10. O usuário deve digitar -1 para avisar que não há mais
notas para inserir. Ao final, o programa deve exibir: a) Quantas notas foram válidas
(digitadas antes do -1); b) A média geral da turma. Cuidado: Se o primeiro valor digitado
já for -1, o programa deve avisar que "Nenhuma nota foi registrada" para evitar o erro
matemático de divisão por zero.
"""

cont = 0
result = 0
avg = 0
note = float(input("Digite a nota do aluno [0 a 10]: "))

while True:
    if note == -1:
        print("Nenhuma nota foi registrada!")
        break
    cont += 1
    result += note
    avg = result / cont

    note = float(input("Digite a nota do aluno [0 a 10]: "))

print(f"A quantidade de alunos na turma: {cont}")
print(f"A media geral de notas da turma: {avg:.2f}")
