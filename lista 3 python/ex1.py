"""
Você foi contratado para programar o sistema de um radar de trânsito.
Construa um programa que leia a velocidade de um carro. Se a velocidade for
estritamente maior que 80 km/h, exiba a mensagem "Veículo multado por excesso de
velocidade!". Independente do carro ter sido multado ou não, o programa sempre deve
exibir ao final a mensagem "Dirija com segurança.".
"""

speed = int(input("Velocidade do carro: "))
limit = 80

if speed > limit:
    print(f"O limite de velocidade é: {limit}km/h. Você estava a {speed}km/h.")
    print("Veiculo multado por excesso de velocidade!")
print("Dirija com segurança.")