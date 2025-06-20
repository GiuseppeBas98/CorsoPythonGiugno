from soldato import Soldato
import random

class Arciere(Soldato):
    def __init__(self, nome):
        super().__init__(nome)
        super().set_costo(100)
        super().set_attacco(150)
        super().set_difesa(50)
        super().set_salute(200)

    def attacca(self, bersaglio):
        if self.vivo():
            print(f"{super().get_nome()} attacca {bersaglio.get_nome()} causando {super().get_attacco()} danni.")
            bersaglio.difendi(super().get_attacco())

    def __str__(self):
        return f"Arciere: {super().__str__()}"