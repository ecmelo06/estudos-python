"""
Dadas duas matrizes A 5x5 e B 5x5 inicializadas pelo usuário via teclado, criar
e imprimir a matriz S sendo a soma de A e B.
"""

linhas = 2
colunas = 2

matrizA = [0] * linhas
for i in range(linhas):
    for j in range(colunas):
        matrizA[i] = [0] * colunas

matrizB = [0] * linhas
for i in range (linhas):
    for j in range (colunas):
        matrizB[i] = [0] * colunas

matrizS = [0] * linhas
for i in range(linhas):
    for j in range(colunas):
        matrizS[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        matrizA[i][j] = int(input(f"[Matriz A] - Digite um valor para linha {i} e para a coluna {j}: "))
        matrizB[i][j] = int(input(f"[Matriz B] - Digite um valor para linha {i} e para a coluna {j}: "))
        matrizS[i][j] = matrizA[i][j] + matrizB[i][j]
       
for i in range(linhas):
    for j in range(colunas):
        print(f"{matrizS[i][j]:3}", end=" ")
    print()