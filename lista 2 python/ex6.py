"""
Construa um programa em Python para ler três valores que representam
três segmentos de reta. Verificar se com esses segmentos é possível compor um triângulo e
mostrar uma mensagem dizendo se é ou não possível. 
"""

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print("Os lados formam um triangulo")
else: 
    print("Os lados não formam um triangulo")