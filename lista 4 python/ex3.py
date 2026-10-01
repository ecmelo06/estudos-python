"""
Um e-commerce precisa calcular o frete do pedido. Leia o estado de destino
(ex: SP, RJ, MG) em formato de texto e o valor total do carrinho (decimal) e apresente o
valor do frete ao usuário conforme as regras a seguir.
Usando a estrutura `match-case` para o estado:
• Se for SP: O “frete é grátis” caso o carrinho seja maior que R$ 100,00.
• Se for RJ ou MG: O frete é grátis caso o carrinho seja maior que R$ 150,00.
• Outros estados e para casos não isentos do frete: Imprima "Frete padrão de
R$ 40,00 aplicado".
"""

city = input("Bem-Vindo ao seu e-commerce\n" \
"Trabalhamos com a possibilidade de Frete gratis ou de acordo com a região, com um valor pré-determinado. \n" \
"Frete grátis para todo o estado de São Paulo. [SP] \n" \
"Para o Rio de Janeiro e Minas Gerais é R$ 50,00 ou Grátis com compra acima de R$ 150,00 [MG / RJ]\n" \
"Para a Região Sul, o frete custa R$ 88,00 ou Grátis com compra acima de R$ 220,00 [RS / SC / PR]\n" \
"Para a Região Norte, o frete custa R$ 104,95 ou Grátis com compra acima de R$ 235,00 [AC / AP / AM / PA / RO / RR / TO] \n" \
"Para a Região Centro-Oeste, o frete custa R$ 92,00 ou Grátis com compra acima de R$ 260,00 [DF / GO / MS / MT] \n" \
"Para a Região Nordeste, o frete custa R$ 112,22 ou Grátis com compra acima de R$ 275,00 [AL / BA / CE / MA / PB / PE / PI / RN / SE] \n" \
"Digite seu estado: ").upper()

match city:
    case 'MG' | 'RJ':
        car = int(input("Digite o valor do seu pedido: "))
        if car > 150:
            print(f"Você é da região sudeste, fora de São Paulo. Seu carrinho acima de R$ 150.00, frete grátis")
        else: 
            value = car + 50
            print(f"Você é da região sudeste, fora de São Paulo, o valor total ficou de: {value:.2f}")
    case 'RS' | 'SC' | 'PR':
        car = int(input("Digite o valor do seu pedido: "))
        if car > 220:
            print(f"Você é da região sul, compras acima de R$ 220,00 tem frete grátis.")
        else:
            value = car + 88
            print(f"Você é da região sul, o valor total ficou de: {value:.2f}")
    case 'AC' | 'AP' | 'AM' | 'PA' | 'RO' | 'RR' | 'TO':
        car = int(input("Digite o valor do seu pedido: "))
        if car > 235:
            print(f"Você é da região norte, compras acima de R$ 235,00 tem frete grátis.")
        else:
            value = car + 104.95
            print(f"Você é da região sul, o valor total ficou de: {value:.2f}")
    case 'DF' | 'GO' | 'MS' | 'MT':
        car = int(input("Digite o valor do seu pedido: "))
        if car > 260:
            print(f"Você é da região centro-oeste, compras acima de R$ 260,00 tem frete grátis.")
        else: 
            value = car + 92
            print(f"Você é da região centro-oeste, o valor total ficou de: {value:.2f}")
    case 'AL' | 'BA' | 'CE' | 'MA' | 'PB' | 'PE' | 'PI' | 'RN' | 'SE':
        car = int(input("Digite o valor do seu pedido: "))
        if car > 275:
              print(f"Você é da região nordeste, compras acima de R$ 275,00 tem frete grátis.")
        else: 
            value = car + 112.22
            print(f"Você é da região nordeste, o valor total ficou de: {value:.2f}")
    case _:
        print("Estado informado incorretamente.")
        exit()