from soldato import Soldato
import random

class Cavaliere(Soldato):
    def __init__(self, nome):
        super().__init__(nome)
        super().set_costo(150)
        super().set_attacco(100)
        super().set_difesa(150)
        super().set_salute(200)

    def attacca(self, bersaglio):
        if self.vivo():
            if random.random() < 0.2:
                danno = super().get_attacco() * 2
                print(f"{super().get_nome()} colpisce {bersaglio.get_nome()} con un colpo critico causando {danno} danni!")
                bersaglio.difendi(danno)
            else:
                print(f"{super().get_nome()} attacca {bersaglio.get_nome()} causando {super().get_attacco()} danni.")
                bersaglio.difendi(super().get_attacco())

    def __str__(self):
        return f"Cavaliere: {super().__str__()}"
    