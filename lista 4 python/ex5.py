"""
Para alugar um carro, a locadora exige regras diferentes por categoria.
Leia a idade do motorista (inteiro), se ele possui CNH válida (booleano) e a
categoria desejada para o aluguel ("Luxo" ou "Popular" em texto) e apresente o resultado
conforme as regras a seguir.
• Para alugar "Luxo", ele precisa de CNH verdadeira E ter 25 anos ou mais. Mensagem
a ser mostrada: “Status: Aluguel da categoria LUXO aprovado!”
• Para alugar "Popular", basta ter a CNH verdadeira (a idade não importa). Mensagem
a ser mostrada: “Status: Aluguel da categoria POPULAR aprovado!”.
• Mensagem padrão para nenhum dos dois casos: “Status: Aluguel Negado. Requisitos
não cumpridos para a categoria escolhida”
"""

print("Bem-Vindo! Na locadora de carros existem 2 categorias de aluguel. \n" \
"1. Carros de Luxo.\n" \
" - Necessário: CNH verdadeira E ter 25 anos ou mais.\n" \
"2. Carros Populares.\n" \
" - Necessário: CNH verdadeira.")
name = input("Digite seu nome: ")
print(f"Bem-Vindo {name}.")
age = int(input("Digite sua idade: "))
if age >= 25:
    print("Você teu direito de alugar nas duas categorias existente. ")
    cnh = input("Sua CNH está válida? ")
    valueCNH = cnh in ['sim', 's', 'Sim', 'SIM', 'S']
    if valueCNH == True:
        value = input("Escolha a categoria [Luxo | Popular]: ")
        match value:
            case "Luxo":
                print("Status: Aluguel da categoria LUXO aprovado!")
            case "Popular":
                print("Status: Aluguel da categoria POPULAR aprovado!")
            case _:
                print("Status: Aluguel Negado. categoria não encontrada")
    else: 
        print("Status: Você precisa ter uma CNH válida para poder alugar um carro!")
else: 
    value = input("Você tem direito apenas a alugar um carro da categoria popular. Continuar [S/N]: ").upper()

    match value: 
        case "S":
            cnh = input("Sua CNH está válida? ")
            valueCNH = cnh in ['sim', 's', 'Sim', 'SIM', 'S']
            if valueCNH == True:
                print("Status: Aluguel na categoria POPULAR aprovado!")
            else:
                print("Status: Você precisa ter uma CNH válida para poder alugar um carro!")
        case "N":
            print("Status: Aluguel Negado. Requisitos não cumpridos para a categoria escolhida")