"""
Um sistema bancário exige um PIN (senha) de 4 dígitos numéricos para
acesso. Crie um programa em Python onde a senha correta seja '9876'. O programa deve
pedir a senha repetidamente enquanto a senha digitada for diferente da correta. Quando
o usuário finalmente acertar, o programa deve exibir a mensagem "Acesso Liberado!".
"""

pinCorrect = 9876

password = int(input("Digite o Pin correto [4 digitos númericos]: "))
while password != pinCorrect:
    password = int(input("Pin incorreto, digite novamente [4 digitos númericos]: "))

    if password == pinCorrect:
        print("Acesso Liberado!")
        break
