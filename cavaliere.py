from soldato import Soldato
import random

class Cavaliere(Soldato):
    def __init__(self, nome):
        super().__init__(nome)
        super().set_costo(150)
        super().set_attacco(100)
        super().set_difesa(150)
        super().set_salute(200)
        self.__difesa_attiva = False # attributo per l'abilità speciale

    def attacca(self, bersaglio):
        if self.vivo():
            if random.random() < 0.2:
                danno = super().get_attacco() * 2
                print(f"{super().get_nome()} colpisce {bersaglio.get_nome()} con un colpo critico causando {danno} danni!")
                bersaglio.difendi(danno)
            else:
                print(f"{super().get_nome()} attacca {bersaglio.get_nome()} causando {super().get_attacco()} danni.")
                bersaglio.difendi(super().get_attacco())

    def difendi(self, danno):
        if self.get_difesa_attiva():
            danno_ridotto = danno / 2
            danno_effettivo = max(0, danno_ridotto - self.get_difesa())
            self.set_salute(self.get_salute() - danno_effettivo)
            print(f"{self.get_nome()} ha attivato la difesa speciale e subisce {danno_effettivo} danni! (Danno originale: {danno}). Salute rimanente: {self.get_salute()}")
            self.difesa_attiva = False  # Resetta l'abilità dopo un turno
        else:
            danno_effettivo = max(0, danno - self.get_difesa())
            self.set_salute(self.get_salute() - danno_effettivo)
            print(f"{self.get_nome()} subisce {danno_effettivo} danni! Salute rimanente: {self.get_salute()}")
        if self.get_salute() <= 0:
            print(f"{self.get_nome()} è stato sconfitto!")  


    # def abilita_speciale(self):
    #     self.difesa_attiva = True
    #     print(f"{self.get_nome()} attiva la difesa speciale! Ridurrà il prossimo danno del 50%.")

    def __str__(self):
        return f"Cavaliere: {super().__str__()}"
    
    def get_difesa_attiva(self):
        return self.__difesa_attiva
    