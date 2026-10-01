"""
Ler uma quantidade indeterminada de duplas de valores (2 valores de
cada vez). Escrever para cada dupla lida uma mensagem que indique se ela foi informada em
ordem crescente ou decrescente. A repetição será encerrada ao ser fornecido valores iguais
para os elementos da dupla.
"""

while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num1 == num2:
        print("Números iguais.")
        break
    elif num1 < num2:
        print(f"{num1}, {num2}. As duplas estão em ordem crescente.")

    else: 
        print(f"{num1}, {num2}. As duplas estão em ordem decrescente.")
   
    
   