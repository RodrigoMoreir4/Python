pratos = []
while True:
    print(f'''Existem {len(pratos)} pratos para lavar.
Digite 'A' ou 'a' para adicionar;
Digite 'D' ou 'd' para retirar.
Pratos para lavar: {pratos}
''')
    contador = input('Operação: ')
    for x in contador:
        if x == 'D' or x == 'd':
            if len(pratos) > 0:
                lavado = pratos.pop(-1)
                print(f'Prato {lavado} foi lavado.')
        elif x == 'A' or x == 'a':
            pratos.append(len(pratos)+1)
        else:
            print('Digite somente os comandos A ou D')
    if len(pratos) == 0:
        print('Não existe pratos para lavar')
        break
