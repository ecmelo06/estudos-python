"""
Construa um programa em Python para ler três valores para os lados de um
triângulo: A, B e C. Verificar se os lados fornecidos formam realmente um triângulo. Se formar,
deve ser indicado o tipo de triângulo: isósceles, escaleno ou equilátero. Para verificar se os
lados fornecidos formam um triângulo: A < B + C e B < A + C e C < A + B. Triângulo isósceles:
possui dois lados iguais (A=B ou A=C ou B=C). Triângulo escaleno: possui todos os lados
diferentes (A<>B e B<>C e A<>C). Triângulo equilátero: possui todos os lados iguais (A=B e
B=C)
"""

lado1 = int(input("Digite o valor do lado A: "))
lado2 = int(input("Digite o valor do lado B: "))
lado3 = int(input("Digite o valor do lado C: "))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print(f"Com os valores informados: {lado1}, {lado2}, {lado3}, é possível criar um triangulo.")
    if lado1 == lado2 and lado3 == lado2:
        print("Triângulo Equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Triângulo Isósceles.")
    else: 
        print("Triângulo Escaleno.")
else:
    print(f"Com os valores informados: {lado1}, {lado2}, {lado3}, não é possível criar um triângulo. ")