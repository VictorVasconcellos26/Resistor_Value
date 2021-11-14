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

resistor_patters = {'0': 'Preto',
                    '1': 'Marrom',
                    '2': 'Vermelho',
                    '3': 'Laranja',
                    '4': 'Amarelo',
                    '5': 'Verde',
                    '6': 'Azul',
                    '7': 'Violeta',
                    '8': 'Cinza',
                    '9': 'Branco'
                    }

while True:
    number = input("Digite o código solicitado: ")
    if len(number) > 3 or len(number) < 3:
        print("Código não suportado, tente novamente.")
    else:
        break


def code():
    multiplier = number[2]
    value_resistor_default = int(number[0] + number[1])
    value_resistor_default = value_resistor_default * int(resistor_colors.setdefault(multiplier))
    value_resistor_index = f"{value_resistor_default:_.1f}"
    value_resistor_index = value_resistor_index.replace('.', ',').replace('_', '.')
    colors_reference()
    print("")
    print(f"O valor do resistor de código ({number}) é de {value_resistor_index} ohms!")
    return


def colors_reference():
    print("""============================
As cores selecionadas foram:
============================
    """)
    for colors in number:
        reference_number = resistor_patters.setdefault(colors)
        print(colors,":",reference_number)
    return


code()
