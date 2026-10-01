"""
Escreva um programa em Python que calcule e mostre na tela os 50
primeiros números primos maiores que 100. Obs.: Um número é considerado primo quando
ele possui exatamente dois divisores inteiros: o número 1 e ele próprio (ou seja, a divisão só
deixa resto zero nesses dois casos). Exemplo: O número 101 é primo, pois só é divisível por 1
e por 101. Já o número 102 não é primo, pois além de 1 e 102, ele também pode ser dividido
por 2, por 3, etc. (Dica: 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373 e 379 são os 50
Primos maiores que 100).
"""
cont = 0
i = 101
k = 101
while cont < 50:
    
    for i in range (i, k + 1, 1):
        
        if k % i== 0:
            cont += 1 
        k += 1
            
        print(f"Os números são: {i}")
print(f"A quantidade de números primos maiores que 100 é: {cont}")
