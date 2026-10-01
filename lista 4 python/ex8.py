"""
Para receber um auxílio estudantil, o estudante precisa preencher um
requisito lógico exato. Ele é aprovado SE: tiver idade entre 18 e 25 anos (inteiro) AND
(possuir bolsa de estudos (booleano) OR o curso deve ser "Tecnologia" (texto)), ou seja,
ele precisa ter a "idade necessária" "e" um dos outros dois critérios. Faça um programa
que solicite todas essas informações ao estudante e que apresente ao final uma
mensagem de Auxílio Aprovado ou Negado. Escreva o código usando os parênteses
corretamente para respeitar essa lógica.
"""

name = input("Bem-Vindo a requisição do seu Auxílio Estudantil. \n" \
"Digite seu nome: ")
print(f"Olá, {name}. \n"
"Para saber se você tem direito ao auxílio, leia a lista abaixo: \n" \
"1. O aluno deve ter entre 18 e 25 anos. \n" \
"2. O aluno deve OU possuir bolsa de estudos OU deve cursar Tecnologia.")
age  = int(input("Digite sua idade: "))
if age < 18 or age >= 25:
    print("Você não se encontra na facha etária para solicitar auxílio estudantil.")
else: 
    scholarship = input("Você possui bolsa de estudos? ").upper()
    verify_scholarship = scholarship in ['SIM', 'S', 'YES']
    string = "TECNOLOGIA"
    tecnology = input("Digite seu curso: ").upper()
    if (string in tecnology) or (verify_scholarship == True):
        print("Você tem direito ao auxílio estudantil.")
    else:
        print("Você não tem direito ao auxílio estudantil.")