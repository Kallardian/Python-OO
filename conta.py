class Conta:
    def __init__(self, numero, titular, saldo, limite): 
        #self is a reference that finds the object in the memory, it is given automatically
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite