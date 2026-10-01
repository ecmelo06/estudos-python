"""
Read an integer number H and print a Christmas Tree with height H.
    e.g.
    Height = 7
          *
         ...
        .....
       .......
      .........
     ...........
    .............
          |
          |
"""
height = int(input("Digite a altura da árvore de natal: "))
qtd = 0
qtdSpaces = 0
resultQtdSpaces = 0

spaces = " "
truckTree = ""
point = ""
stars = ""

for i in range(height):
    point = ""
    spaces = ""
    stars = ""
    qtdSpaces = height - 1
    qtd = (2 * i) - 1
    if (qtd == 1):
        for m in range(qtdSpaces):
            resultQtdSpaces = m
            spaces += " "
            stars = "*"
        print(f"{spaces}{stars}")
    else:
        for k in range (qtdSpaces):
             spaces += " "
        for j in range(qtd):
            point += "."
        print(f"{spaces}{point}")

for n in range(2):
    spaces = ""
    for y in range(resultQtdSpaces):
        truckTree = "|"
        spaces += " "
    print(f"{spaces}{truckTree}")