from abc import ABC, abstractmethod

class Soldato(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self.__costo = 100
        self.__attacco = 100
        self.__difesa = 100
        self.__salute = 200

    @abstractmethod
    def attacca(self, bersaglio):
        pass

    def difendi(self, danno):
        danno_effettivo = max(0, danno - self.__difesa)
        self.set_salute(self.__salute - danno_effettivo)
        print(f"{self.__nome} subisce {danno_effettivo} danni! Salute rimanente: {self.__salute}")
        
    def vivo(self):
        return self.__salute > 0

    def __str__(self):
        return f"{self.__nome} (Costo: {self.__costo}, Attacco: {self.__attacco}, Difesa: {self.__difesa}, Salute: {self.__salute})"

    def stato(self):
        return f"{self.__nome} - Salute: {self.__salute}, Ruolo: {self.__class__.__name__}"

    # Getter e Setter per nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, value):
        self.__nome = value

    # Getter e Setter per costo
    def get_costo(self):
        return self.__costo

    def set_costo(self, value):
        self.__costo = value

    # Getter e Setter per attacco
    def get_attacco(self):
        return self.__attacco

    def set_attacco(self, value):
        self.__attacco = value

    # Getter e Setter per difesa
    def get_difesa(self):
        return self.__difesa

    def set_difesa(self, value):
        self.__difesa = value

    # Getter e Setter per salute
    def get_salute(self):
        return self.__salute

    def set_salute(self, value):
        self.__salute = value

