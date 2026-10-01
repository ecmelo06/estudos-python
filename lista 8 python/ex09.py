"""
Escreva um programa que crie, em tempo de compilação, 2 vetores (A e B)
de 10 elementos inteiros cada. Após isso, o programa deverá criar um terceiro vetor (C),
de 20 posições, que seja a união dos dois primeiros, ou seja, as primeiras 10 posições de
C recebem o vetor A, e as últimas 10 recebem o vetor B. Mostre o vetor resultante.
"""

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

C = A + B 

print(C)