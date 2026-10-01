"""
Crie uma função chamada validar_senha(senha) que receba uma string
como parâmetro. A função deve retornar True, se a senha for forte, ou False se for fraca,
baseada nestas regras: ter pelo menos 8 caracteres e NÃO ser “12345678” nem conter a
palavra “senha” (independente de maiúsculas/minúsculas). No programa principal, use um
laço de repetição while para pedir e validar uma senha continuamente até a função de
validação da senha retornar True.
"""

def validar_senha(senha):
    if len(senha) < 8:
        return False
    

senha = input("Digite sua senha: ")
teste = validar_senha(senha)
print(teste)