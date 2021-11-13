resistor_colors = {'0': '1',
                   '1': '10',
                   '2': '100',
                   '3': '1000',
                   '4': '10000',
                   '5': '100000',
                   '6': '1000000',
                   '7': '10000000',
                   '8': '100000000',
                   '9': '1000000000'
                   }

while True:
    number = input("Digite o código solicitado: ")
    if len(number) > 3 or len(number) < 3:
        print("Código não suportado, tente novamente.")
    else:
        break


def code():
    multiplier = number[2]
    valor_resistor = int(number[0] + number[1])
    valor_resistor = valor_resistor * int(resistor_colors.setdefault(multiplier))
    valor_resistor2 = f"{valor_resistor:_.1f}"
    valor_resistor2 = valor_resistor2.replace('.', ',').replace('_', '.')
    print(f"O valor do resistor de código ({number}) é de {valor_resistor2} ohms!")
    return


code()
