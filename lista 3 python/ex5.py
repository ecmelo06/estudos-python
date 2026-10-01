"""
Construa um mini-filtro de spam. O programa deve pedir ao usuário para
digitar o assunto de um e-mail. Se a palavra "GRÁTIS" estiver no assunto, o sistema
deve alertar "CUIDADO: Possível Spam detectado!". Caso contrário, exiba "Assunto
limpo.".
"""

print("Bem-Vindo ao seu e-mail institucional")
title = input("Escreva o Titulo do seu E-mail: ")
body  = input("Escreva o Assunto do seu E-mail: ")
spam = "grátis"

if spam.upper() in body.upper():
    print("CUIDADO: Possível Spam detectado!")
else:
    print("Assunto Limpo")
