"""
Crie um programa em Python que funcione como uma pesquisa contínua,
solicitando o sexo ('M' para Masculino ou 'F' para Feminino) e a idade de várias pessoas, uma
de cada vez. O programa deve ser encerrado imediatamente se o usuário digitar qualquer
valor diferente de 'M' ou 'F' no momento de informar o sexo. Ao final, quando a repetição
parar, o algoritmo deve calcular e exibir: a) A média de idade dos homens cadastrados. b) A
média de idade das mulheres cadastradas." Dica: Lembre-se de que a média é a soma das
idades dividida pela quantidade de pessoas. Mas o que acontece no seu cálculo se nenhum
homem (ou nenhuma mulher) for registrado? Evite o erro matemático de "divisão por zero"!"
"""

gen = input("Digite seu gênero: ").upper()
age = int(input("Digite sua idade: "))
consultGen = ['M', 'F']
ageMan = 0
contMan = 0
ageWomen = 0
contWomen = 0
avgMan = 0
avgWomen = 0

valityGen = gen in consultGen

while valityGen != False:
    if gen == 'M':
        ageMan += age
        contMan += 1
        avgMan = ageMan / contMan
    if gen == 'F':
        ageWomen += age
        contWomen += 1
        avgWomen = ageWomen / contWomen

    
    gen = input("Digite seu gênero: ").upper()
    consultGen = ['M', 'F']
    valityGen = gen in consultGen
    if valityGen == False:
        print("Gênero inválido.")
        print("\n")
        break
    else:
        age = int(input("Digite sua idade: "))

    
print(f"Quantidade de Homens declarados na pesquisa: {contMan}\n"
f"A media de idade de homens: {avgMan}")
print("\n")
print(f"Quantidade de Mulheres declaradas na pesquisa: {contWomen}\n"
f"A media de idade de Mulheres: {avgWomen}")
        
    