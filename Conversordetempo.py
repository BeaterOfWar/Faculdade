class Conversor:
    def __init__(self, segundos):
        self.segundos = segundos

    def resolver (self):
        self.restosegundos = self.segundos%60
        self.minutos = self.segundos//60
        self.restominutos = self.minutos%60
        self.horas = self.minutos//60
        print (f'{int(self.horas)}:{int(self.restominutos)}:{int(self.restosegundos)}')

receber = Conversor(int(input()))
receber.resolver()