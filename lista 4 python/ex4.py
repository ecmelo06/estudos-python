"""
Um sistema de segurança não permite senhas óbvias. Peça ao usuário
para criar uma senha (texto). Se a palavra "admin" (em qualquer formato,
ignorando maiúsculas) OU a sequência "123" estiverem dentro da senha digitada,
exiba "Erro: Senha fraca detectada!". Caso contrário, exiba "Senha configurada".
"""

print("Bem-Vindo ao seu gerador de senhas seguras, mas ainda sem criptografia.\n" \
"Você deve ter os seguintes requisitos para fazer uma senha segura: \n" \
"1. Ter pelo menos 8 digitos. \n" \
"2. Não pode conter partes do teu nome (nome ou sobrenome)\n" \
"3. Não pode ter a sequencia: 123. \n" \
"4. Não pode ter a palavra admin contida nela.")
name    = input("Digite seu nome: ")
surname = input("Digite seu sobrenome: ")

password      = input("Digite sua senha: ").upper()

verifyLenPass = len(password)
verifyName    = name.upper() in password.upper()
verifySurname = surname.upper() in password.upper()
verifyStr     =  'ADMIN'
verifyNum     = '123'
verifyProhibite = verifyStr in password.upper() or verifyNum in password


if verifyLenPass < 8:
    print("A senha não deve ter menos de 8 digitos.")
else:
    if verifyName == True:
        print("Erro: Senha fraca detectada. Você não pode utilizar teu nome na criação de uma senha.")
    elif verifySurname == True:
        print("Erro: Senha fraca detectada. Você não pode utilizar teu sobrenome na criação de uma senha.")
    elif verifyProhibite == True: 
        print("Erro: Não pode conter [ADMIN] ou a sequência [123] na senha")
    else:
        print(f"Bem-Vindo, {name} {surname}. Senha configurada.")


