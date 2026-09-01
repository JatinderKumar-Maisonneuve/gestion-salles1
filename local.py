class Local:
    def __init__(self,numero,capacite):
        self.numero = numero
        self.capacite = capacite

    def __str__(self):
        return f"Local {self.numero} | capacité {self.capacite} places."