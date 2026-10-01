"""
Elabore um programa que leia pelo teclado um vetor de 6 posições de
números inteiros. Após a leitura, exiba o menu a seguir e peça para o usuário digitar uma
variável identificadora (1, 2, 3 ou 4). O programa deve calcular a operação correspondente
à opção escolhida:
Escolha a opção desejada:
1. Soma dos elementos
2. 2- Produto (multiplicação) dos elementos
3. 3- Média dos elementos
4. 4- Mostrar o vetor
5. ?
"""

vet = [0] * 6
for i in range(len(vet)):
    num = int(input("Digite um valor: "))
    vet[i] = num


opcao = int(input(" \n" \
"1. Soma dos elementos. \n" \
"2. Produto dos elementos. \n" \
"3. Media dos elementos \n" \
"4. Mostrar Vetor. \n" \
"5. Sair. \n" \
"Escolha a opção desejada: "))

soma = 0
produto = 1
media = 0
match opcao:
        case 1:
            for i in range(len(vet)):
               soma += vet[i]
            print(f"A soma dos elementos do vetor é: {soma}")
        case 2:
            for i in vet:
                produto *= i
            print(f"O produto dos elementos do vetor é: {produto}")

        case 3: 
            for i in vet:
                produto *= i
                media = produto / len(vet)
            print(media)  
        case 4: 
            print(f"Vetor: {vet}")
        case 5:
            print("Saindo.")
            exit()
        case _:
            print("Opção inválida. Saindo.")
            exit()