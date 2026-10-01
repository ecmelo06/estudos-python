"""
Em um jogo, para o personagem usar o "Ataque Especial", ele precisa
de três coisas: ter energia maior ou igual a 80 (inteiro), estar com a arma
"Espada" (texto) e NÃO estar envenenado (booleano). Crie um programa que leia
esses três dados digitados pelo usuário e use um único `if` para verificar se
o ataque foi realizado com sucesso ou se falhou. As opções de armas devem ser:
"Espada", "Faca" e "Martelo".
"""

name = input("Bem-Vindo ao seu jogo de RPG: CATACUMBAS E KOMODO\n" \
"Digite o nome do seu personagem: ")
health = input("Você está envenenado: [S/N] ")
value_health = health in ['nao', 'no', 'n', 'não', 'NAO', 'N', 'NO']
if value_health == True:
    energy = int(input("Quanto de energia você tem? [0-100]: "))
    if energy >= 80:
        equipment = int(input("Qual arma você está utilizando?\n" \
        "1 - Espada\n" 
        "2 - Faca\n" 
        "3 - Martelo \n" \
        "Arma: "))
        match equipment:
            case 1:
                print("Ataque especial foi realizado com sucesso.")
            case 2:
                print("Ataque especial falhou. Você só pode utilizar Espada para realizar o ataque especial.")
            case 3:
                print("Ataque especial falhou. Você só pode utilizar Espada para realizar o ataque especial.")
            case _:
                print("Ataque especial falhou. Arma não selecionada.")
                exit()
    else:
        print("Ataque especial falhou. Você deve ter pelo menos 80 de energia.")
        
else: 
    print("Ataque especial falhou. Você não pode estar envenenado.")    