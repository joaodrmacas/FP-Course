class automovel():
    def __init__(self,capacity,combustivel,consumo):
        self.capacity = capacity
        self.combustivel = combustivel
        self.consumo = consumo
    
    def combustivel(self):
        return self.combustivel
    
    def autonomia(self):
        return int(self.combustivel*100//self.consumo)

    def abastece(self,n_litros):
        novo = self.combustivel+n_litros
        if novo > self.capacity:
            raise ValueError("Excedeu o deposito")
        self.combustivel = novo
        return "{} Km até abastecimento".format(self.autonomia())

    def percorre(self,n_km):
        combustivel_nec = n_km * self.consumo / 100
        if self.combustivel - combustivel_nec < 0:
            raise ValueError("Tanque nao suficiente")
        self.combustivel -= combustivel_nec
        return "{} Km até abastecimento".format(self.autonomia())
