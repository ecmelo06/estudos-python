"""
Imagine um sistema de alarme de uma loja. Existe uma variável booleana
chamada 'loja_aberta'. Se a loja NÃO estiver aberta (use o operador lógico de negação),
o programa deve imprimir "Alarme ativado!". Se estiver, deve imprimir "Alarme
desativado".
"""

print("SISTEMA DE SEGURANÇA DE SUA LOJA\n" \
"Horário de Funcionamento: Das 8h às 20h.")

open = input("A loja está aberta? ")
isOpen = open in ['sim', 's', 'SIM', 'S', 'TRUE', 'true', 't', 'T']
if isOpen != True:
    print("Alarme ativado!")
else:
    print("Alarme desativado!")