from soldato import Soldato
from random import randint

class Mago(Soldato):
    def __init__(self, nome):
        super().__init__(nome)
        super().set_costo(150)
        super().set_attacco(0)
        super().set_difesa(50)
        super().set_salute(200)

    def attacca(self, bersaglio):
         if self.vivo():
            num = randint(150, 250)
            danno = super().get_attacco() + num
            print(f"{super().get_nome()} colpisce {bersaglio.get_nome()} con una palla di fuoco causando {danno} danni!")
            bersaglio.difendi(danno)
    def __str__(self):
        return f"Mago: {super().__str__()}"
    
    # def abilita_speciale(self, bersaglio):
    #     pass