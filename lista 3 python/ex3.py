"""
Um clube de natação divide seus atletas em categorias pela idade. Construa
um programa que leia a idade do nadador e classifique-o da seguinte forma:
● Menor de 12 anos: "Categoria Infantil"
● De 12 a 17 anos: "Categoria Juvenil"
● 18 anos ou mais: "Categoria Adulto"
"""

age = int(input("Digite sua idade: "))

if age <= 0:
    print("Valor inválido.")
elif age < 12:
    print("Categoria Infantil.")
elif age >= 12 and age <= 17:
    print("Categoria Juvenil.")
else: 
    print("Categoria Adulto.")

