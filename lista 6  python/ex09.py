"""
Escreva um programa em Python que use um laço infinito (while True)
para ler números do teclado. Regras: 1) Se o usuário digitar um número negativo, ignore-
o, avise "Número inválido ignorado" e vá para a próxima leitura usando 'continue'. 2) Se o
usuário digitar o número 999, o programa deve ser interrompido imediatamente usando
'break'. 3) Se digitar um número positivo normal, adicione-o a uma soma total. No final
(fora do laço), imprima a soma dos números válidos aceitos.
"""

cont = 0
soma = 0

num = int(input("Digite um valor: "))
while True:
    if num == 999:
        break
    elif num < 0:
        print("Número negativo ignorado!")
        num = int(input("Digite um valor: "))
        continue
        
    else:
        cont += 1
        soma += num 
    num = int(input("Digite um valor: "))

print(f"A soma dos números é: {soma}")