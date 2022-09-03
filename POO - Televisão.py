class Televisão:
    def __init__(self,min=1,max=99):
        while True:
            try:
                self.min = int(input('Digite o Canal mínimo: '))
                break
            except ValueError:
                self.min = min
                break
        while True:
            try:
                self.max = int(input('Digite o Canal máximo: '))
                break
            except ValueError:
                self.max = max
                break
        while True:
            try:
                self.canal = int(input('Digite um canal para iniciar: '))
                if self.min <= self.canal <= self.max:
                    break
                else:
                    print(f'Digite um valor entre {self.min} e {self.max}: ')
            except ValueError:
                print('Informe um canal!')
        self.cmin = self.min
        self.cmax = self.max
    def muda_canal_para_baixo(self):
        self.canal -= 1
        if self.canal < self.cmin:
            self.canal = self.cmax
    def muda_canal_para_cima(self):
        self.canal += 1
        if self.canal > self.cmax:
            self.canal = self.cmin
       
tv = Televisão()
try:
    for x in range(0, int(input('Quantos canais vocês quer subir? '))):
        tv.muda_canal_para_cima()
        print(f'Canal: {tv.canal}')
except ValueError:
    pass
try:
    for x in range(0, int(input('Quantos canais você quer descer? '))):
        tv.muda_canal_para_baixo()
        print(f'Canal: {tv.canal}')
except ValueError:
    pass