from soldato import Soldato

class Guaritore(Soldato):
    def __init__(self, nome):
        super().__init__(nome)
        super().set_costo(100)
        super().set_attacco(0)
        super().set_difesa(50)
        super().set_salute(200)
    
    def attacca(self, alleato):
        if self.vivo():
            cura_effettiva = 100
            alleato.set_salute(cura_effettiva)
            print(f"{super().get_nome()} cura {alleato.get_nome()} per {cura_effettiva} salute.")

    def __str__(self):
        return f"Guaritore: {super().__str__()}"

    # def abilita_speciale(self, bersaglio):
    #     pass