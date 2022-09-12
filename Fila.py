fila = []
último = 0
while True:
    print(f'''Existem {len(fila)} clientes na Fila;
Fila atual: {fila}
Digite A para atendimento na Fila;
Digite F para chegada de clientes na Fila;
Digite S para sair.
''')
    contador = input('Digite Operação para Fila: ')
    for x in contador:
        if x == 'A' or x == 'a':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} da Fila atendido')
            else:
                print('Fila vazia! Ninguém para atender.')
        elif x == 'F' or x == 'f':
            último+= 1
            fila.append(último)
        elif x == 'S' or x == 's':
            break
        else:
            print('Operação inválida na Fila: Digite apenas F, A ou S!')
    if x == 'S' or x == 's':
        break
print('Você saiu do programa!')