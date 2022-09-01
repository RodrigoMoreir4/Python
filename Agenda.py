agenda = []
def pede_nome():
    while True:
        y = True
        n = input('Nome: ')
        for x in list(n):
            if x == '#':
                print('Esse caractere "#" não é aceito no Nome!' )
                y = False
        if n == "":
            print('Digite um Nome!')
            y = False
        elif y == True:
            return n

def pede_telefone():
    while True:
        z = True
        t = input('Telefone: ')
        for o in list(t):
            if o == '#':
                print('Esse caractere "#" não é aceito no Telefone!')
                z = False
        if z == True:
            return t

def mostra_dados(nome, telefone):
    print(f'Nome: {nome} | Telefone: {telefone}')

def pede_nome_arquivo():
    return input('Nome do arquivo: ')

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    n = True 
    for x in agenda:
        if x[0] == nome:
            print('Esse contato já existe!')
            n = False
    if n == True:
        agenda.append([nome, telefone])        

def apaga():
    confirmação = input('"S" para confirmar ou "M" para voltar ao MENU: ')
    if confirmação == 'S' or confirmação == 's':
        global agenda
        nome = pede_nome()
        p = pesquisa(nome)
        if p is not None:
            del agenda[p]
        else:
            print('Não encontrado!')
    elif confirmação == 'M' or confirmação == 'm':
        menu()
    else:
        print('Escolha "S" ou "M"')

def altera():
    confirmação = input('"S" para confirmar ou "M" para voltar ao MENU: ')
    if confirmação == 'S' or confirmação == 's':
        p = pesquisa(pede_nome())
        if p is not None:
            nome = agenda[p][0]
            telefone = agenda[p][1]
            print('Encontrado:')
            mostra_dados(nome,telefone)
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
        else:
            print('Nome não encontrado!')
    elif confirmação == 'M' or confirmação == 'm':
        menu()
    else:
        print('Escolha "S" ou "M"')

def lista():
    print('\nAgenda\n\n.....')
    for y, e in enumerate(agenda):
        print(f'Contato nº {y+1}:')
        mostra_dados(e[0], e[1])
    print('.....\n')

def tamanho_lista():
    return print(f'O tamanho da Agenda é: {len(agenda)}')

def lê():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#')
            agenda.append([nome, telefone])

def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')

def ordenar_lista():
    agenda.sort()
    for x in agenda:     
        print(f'{x[0]} | Telefone: {x[1]}')

def valida_faixa_inteiro(pergunta, início, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if início <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {início} e {fim}.')

def menu():
    print('''
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Tamanho da Agenda
8 - Ordenar Lista
0 - Sai
''')
    return valida_faixa_inteiro('Escolha uma opção: ',0,8)

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        tamanho_lista()
    elif opção == 8:
        ordenar_lista()
    