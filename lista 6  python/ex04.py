"""
Crie um programa em Python que use um laço 'for' para percorrer os
números de 1 a 30. O programa deve imprimir os números na tela, MAS deve pular todos
os números que são múltiplos de 3. REGRA: Você deve obrigatoriamente usar o comando
'continue' para ignorar os múltiplos de 3, pulando direto para a próxima iteração.
"""

i = 1
for i in range (i, 31):
    if i % 3 == 0:
        continue
    print (i)