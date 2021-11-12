resistor_cores = {'Preto': '0',
                  'Marrom': '1',
                  'Vermelho': '2',
                  'Laranja': '3', 'Amarelo': '4',
                  'Verde': '5',
                  'Azul': '6',
                  'Violeta': '7',
                  'Cinza': '8',
                  'Branco': '9'
                  }


def codigo():
    numero = input("Digite o código solicitado: ")
    valor_resistor = int(numero[0] + numero[1])
    valor_resistor = valor_resistor * int(numero[2])
    print(valor_resistor)
    return


codigo()
