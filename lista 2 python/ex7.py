"""
Escreva um programa em Python para ler o número de eleitores de um
município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que
cada um representa em relação ao total de eleitores. (DICA: regra de três para calcular o
percentual de cada voto em relação ao número de eleitores que é 100%, ou seja, X = (brancos
ou nulos ou validos) * 100 / eleitores)
"""

eleitores = int(input("Número de eleitores: "))
if eleitores <= 0:
    print("Valor inválido. O número de eleitores não pode ser 0.")
else: 
    votosBrancos = int(input("Número de votos em branco: "))
    if votosBrancos > eleitores: 
        print("Valor inválido. O número de VOTOS BRANCOS não pode ser maior que o número de eleitores")
    else: 
        votosNulos = int(input("Numero de votos nulos: "))
        votosValidos = int(input("Número de votos válidos: "))
        if votosValidos <= 0: 
            print("Valor inválido. O número de VOTOS VÁLIDOS não pode ser menor que 0.")
        elif votosValidos > eleitores or votosBrancos > eleitores or votosNulos > eleitores:
            print("O número de votos BRANCOS ou NULOS ou VALIDOS, não podem ser maior que o número de eleitores.")
        else: 
            totVotBrancos = votosBrancos * (100/eleitores)
            totVotNulos = votosNulos * (100/eleitores)
            totVotValidos = votosValidos * (100/eleitores)
            print(f"Quantidade de eleitores: {eleitores:.2f}")
            print(f"Total de votos em branco: {totVotBrancos:.2f}%")
            print(f"Total de votos nulos: {totVotNulos:.2f}%")
            print(f"Votal de votos validos: {totVotValidos:.2f}%")

    