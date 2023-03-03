
class Conta:

    ##Criando atrbutos
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ##métodos abaixos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))



    def deposita(self, valor):
        self.__saldo += valor


    def __pode_sacar(self, valor_para_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_para_sacar <= valor_disponivel_saque


    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite.".format(valor))


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def get_saldo(self):
        return self.__saldo


    @property
    def get_titular(self):
        return self.__saldo


    @property
    def limite(self):
        return self.__limite


    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

