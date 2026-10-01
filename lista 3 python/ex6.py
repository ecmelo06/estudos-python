"""
Um banco aprova financiamentos baseados em regras estritas. O cliente
consegue o empréstimo SE possuir renda maior que 5000 OU apresentar um fiador
(True), MAS APENAS SE o nome estiver limpo no SPC (True). Escreva a lógica
combinando operadores lógicos e parênteses.
"""

print("Bem-Vindo ao setor de financeamento do Banco X")
name = input("Informe seu nome: ")
print(f"Olá, {name}.")
print("Para fazer um financiamento, você deve ter uma renda acima de 5000 ou precisa de um fiador. \n" \
"Além disso, é fundamental que você não tenha nome sujo no SPC.")

""""""
cleanName = input("Você tem alguma dívida no SPC? [S/N]: ")
approveSPC = cleanName in ['Nao', 'nao', 'n', 'Não', 'não',  'NAO', 'NÃO']  
if approveSPC == True:
        income = float(input("Informe sua renda: R$ "))
        guarantor = input("Você tem um fiador? [S/N]: ")
        hGuarantor = guarantor in ['Sim', 's', 'sim', 'S', 'SIM']
        if hGuarantor == True:
            print("Financiamento Aprovado, pelo motivo de haver Fiador.")
        elif income > 5000:
            print("Financiamento Aprovado. Renda maior ou igual a R$ 5000.00.")
        elif income < 5000 and hGuarantor != True:
            print("Financiamento negado! Não tem renda necessária nem fiador.")
else:
    print("Impossível financiamento sem ter o nome limpo no SPC.")