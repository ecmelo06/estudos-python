name = input("Digite seu nome: ")
print(f"Bem-Vindo, {name}.")
nivel = int(input("Digite o seu nível de acesso: "))
status = input("Digite se o status está ativo ou não [SIM / NÃO]:  ").upper()
admin = input("Você é adminstrador [SIM / NÃO]? ").upper()

"""" Até agora eu apenas crei uma forma de receber os valores inseridos pelo usuário"""

nivel_status = status in ['SIM', 'S']
""" Aqui eu verifico se o que foi digitado pelo usuário, está dentro das expecificações que eu determinei. 
    Caso esteja, ele retorna o nivel_acess como verdadeiro. Isso é uma verificação booleana."""
is_admin = admin in ['SIM', 'S']
""" Aqui eu faço a mesma logica que a anterior, a variavel is_admin retorna verdadeiro caso o que o 
    usuário digite esteja dentro dessa expecificação."""



resultado = (nivel >= 5 and status == "S") or not (is_admin == False)
"""O resultado é analisado pela maquina, sempre da esquerda para a direita. 
   A primeira verificação é se o nível de acesso é maior que 5 [Vamos utilizar o valor 6]
   caso seja, retorna True. Caso não, retorna False. Após isso, tem a condição and. Relembrando, para que seja True com o operador 
   and, as duas operações devem ser true. Qualquer uma das duas sendo falsas, retorna False essa operação 
   (lembrando, estamos falando do que está ocorrendo dentro dos parenteses). Continuando, seguindo com as duas operações como verdadeira, temos os operadores 
   or e not. Or == Ou, e o not (não) inverte a expressão booleana atribuida. Neste caso, é False, not False == True. 
   O or ele requer que uma das duas operações seja True, retorna True. """
print(resultado)