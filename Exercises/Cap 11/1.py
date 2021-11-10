class estacionamento():
    def __init__(self,lotacao):
        self.lotacao = lotacao
    def entra(self):
        self.lotacao -= 1
    def sai(self):
        self.lotacao += 1
    def lugares(self):
        return self.lotacao

ist = estacionamento(20)
ist.entra()
ist.entra()
ist.entra()
ist.entra()
ist.sai()
print(ist.lugares())
