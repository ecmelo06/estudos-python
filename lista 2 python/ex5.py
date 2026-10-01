"""
Construa um programa em Python para ler um valor, verificar se está no
intervalo (100, 200) e mostrar essa informação.
"""

n1 = int(input("Digite um valor: "))

if n1 > 100 and n1 < 200:
    print(f"O valor digitado: {n1}, está no intervalor (100, 200).")
elif n1 < 100:
    print(f"O valor digitado: {n1}, não está no intervalor (100, 200).")
else: 
    print(f"O valor digitado: {n1}, não está no intervalor (100, 200).")