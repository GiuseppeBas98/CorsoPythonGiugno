from cavaliere import Cavaliere
from arciere import Arciere
from mago import Mago
from guaritore import Guaritore
import random 
from random import choice
import time

class Esercito:
    def __init__(self):
        self.monete = 1000

    def get_monete(self):
        return self.monete
    
    def crea_esercito(self):
        print("Benvenuto alla creazione del tuo esercito, hai a disposizione 1000 monete per formare il tuo esercito!")
        squadra1 = []
        while True:
            opzione = input("Inserire il tipo di soldato da aggiungere al tuo esercito (1 per Cavaliere, 2 per Arciere, 3 per Mago o 4 per Guaritore): ")
            if opzione == '1':
                soldato = Cavaliere(input("Inserisci il nome del Cavaliere: "))
                squadra1.append(soldato)
                self.monete -= soldato.get_costo()
            elif opzione == '2':
                soldato = Arciere(input("Inserisci il nome dell'Arciere: "))
                squadra1.append(soldato)
                self.monete -= soldato.get_costo()
            elif opzione == '3':
                soldato = Mago(input("Inserisci il nome del Mago: "))
                squadra1.append(soldato)
                self.monete -= soldato.get_costo()
            elif opzione == '4':
                soldato = Guaritore(input("Inserisci il nome del Guaritore: "))
                squadra1.append(soldato)
                self.monete -= soldato.get_costo()
            else:
                print("Opzione non valida. Riprova.")
                continue
            scelta = input(f"Hai speso {soldato.get_costo()} monete. Ti sono avanzati {self.monete} monete.\nVuoi continuare ad inserire soldati? (s/n): ")
            if scelta.lower() == 'n':
                break

            if self.monete < 100:
                print(f"Non hai abbastanza monete per un nuovo soldato. Monete rimaste: {self.monete}")
                break
        
        return squadra1, self.monete
    
    def genera_esercito_random(esercito, budget):
        tipi_soldato = [Cavaliere, Arciere, Guaritore, Mago]

        nomi_possibili = [
            "Thorin", "Eldrin", "Seraph", "Kael", "Lyra", "Morgul", "Alaric",
            "Bryn", "Fael", "Zarek", "Nyra", "Cedric", "Luna", "Dorian", "Ayla",
            "Bronno", "Fantis", "Zaraki", "Yama", "Diggory", "Harry", "Michael", "Marias"
        ]

        usati = set()

        def genera_nome():
            while True:
                nome = random.choice(nomi_possibili)
                if nome not in usati:
                    usati.add(nome)
                    return nome

        while budget >= 100:
            tipo = random.choice(tipi_soldato)

            if tipo == Cavaliere and budget >= 150:
                soldato = Cavaliere(nome=genera_nome())
                budget -= 150

            elif tipo == Arciere and budget >= 100:
                soldato = Arciere(nome=genera_nome())
                budget -= 100

            elif tipo == Guaritore and budget >= 100:
                soldato = Guaritore(nome=genera_nome())
                budget -= 100

            elif tipo == Mago and budget >= 150:
                soldato = Mago(nome=genera_nome())
                budget -= 150

            else:
                continue

            esercito.append(soldato)

        return esercito, budget
    
    def esegui_round(esercito_giocatore, esercito_ia):
        print("\n--- INIZIO ROUND ---")

        max_len = max(len(esercito_giocatore), len(esercito_ia))

        for i in range(max_len):
            soldato_g = esercito_giocatore[i] if i < len(esercito_giocatore) else None
            soldato_ia = esercito_ia[i] if i < len(esercito_ia) else None

            if soldato_g and soldato_ia:
                print(f"\nScontro tra {soldato_g.get_nome()} ({type(soldato_g).__name__}) vs {soldato_ia.get_nome()} ({type(soldato_ia).__name__})")

                # Arciere attacca per primo
                if isinstance(soldato_g, Arciere) and not isinstance(soldato_ia, Arciere):
                    Esercito.esegui_azione(soldato_g, esercito_giocatore, esercito_ia)
                    if soldato_ia.vivo():
                        Esercito.esegui_azione(soldato_ia, esercito_ia, esercito_giocatore)

                elif isinstance(soldato_ia, Arciere) and not isinstance(soldato_g, Arciere):
                    Esercito.esegui_azione(soldato_ia, esercito_ia, esercito_giocatore)
                    if soldato_g.vivo():
                        Esercito.esegui_azione(soldato_g, esercito_giocatore, esercito_ia)

                # SE NON CI SONO ARCERI, SI PASSA ALLA FUNZIONE ESEGUI AZIONE, CHE CONTROLLA LA CURA DEL GUARITORE E LA POSSIBILITà DEL MAGO DI SALTARE IL TURNO
                # INFINE SE NON CI SONO ARCERI O GUARITORI O MAGHI, SI EFFETTUA L'ATTACCO NORMALE
                else:
                    Esercito.esegui_azione(soldato_g, esercito_giocatore, esercito_ia)
                    if soldato_ia.vivo():
                        Esercito.esegui_azione(soldato_ia, esercito_ia, esercito_giocatore)
        
            elif soldato_g and not soldato_ia:
                print(f"\n{soldato_g.get_nome()} non trova un avversario diretto.")
                Esercito.esegui_azione(soldato_g, esercito_giocatore, esercito_ia)

            elif soldato_ia and not soldato_g:
                print(f"\n{soldato_ia.get_nome()} non trova un avversario diretto.")
                Esercito.esegui_azione(soldato_ia, esercito_ia, esercito_giocatore)

        # questo rimuove i soldati morti da entrambi gli eserciti
        esercito_giocatore[:] = [s for s in esercito_giocatore if s.vivo()]
        esercito_ia[:] = [s for s in esercito_ia if s.vivo()]

        print(f"\nFine round: Giocatore ha {len(esercito_giocatore)} soldati, IA ne ha {len(esercito_ia)}\n")
        return esercito_giocatore, esercito_ia
    

    def esegui_azione(soldato, esercito_alleato, esercito_nemico):
        if isinstance(soldato, Guaritore):
            alleati_vivi = [s for s in esercito_alleato if s.vivo() and s != soldato]
            if alleati_vivi:
                bersaglio = random.choice(alleati_vivi)
                soldato.attacca(bersaglio)
            else:
                print(f"{soldato.get_nome()} non ha alleati da curare.")

        elif isinstance(soldato, Mago):
            if random.random() < 0.25:
                print(f"{soldato.get_nome()} è stanco e salta il turno!")
            else:
                if esercito_nemico:
                    nemici_vivi = [s for s in esercito_nemico if s.vivo()]
                    if nemici_vivi:
                        bersaglio = random.choice(nemici_vivi)
                        soldato.attacca(bersaglio)
        
        # elif isinstance(soldato, Cavaliere): # blocco per il Cavaliere
        #     if not soldato.get_difesa_attiva():
        #         soldato.abilita_speciale()
        #     else:
        #         if esercito_nemico:
        #             nemici_vivi = [s for s in esercito_nemico if s.vivo()]
        #             if nemici_vivi:
        #                 bersaglio = random.choice(nemici_vivi)
        #                 soldato.attacca(bersaglio)
        
        else: # Tutti gli altri tipi di soldati
            if esercito_nemico:
                nemici_vivi = [s for s in esercito_nemico if s.vivo()]
                if nemici_vivi:
                    bersaglio = random.choice(nemici_vivi)
                    soldato.attacca(bersaglio)

    
    def acquista_soldati(esercito, budget, is_giocatore):                
        if is_giocatore:
            print("\n*** Fase di acquisto di soldati del giocatore***")
            print(f"Budget disponibile: {budget} monete")
            while True:
                if budget < 100:
                    print(f"Non hai abbastanza monete per un nuovo soldato. Monete rimaste: {budget}")
                    break

                opzione = input("Inserire il tipo di soldato da aggiungere al tuo esercito (0 per USCIRE, 1 per Cavaliere, 2 per Arciere, 3 per Mago o 4 per Guaritore: ")
                if opzione == '0':
                    print("Uscita dalla fase di acquisto.")
                    break
                elif opzione == '1':
                    soldato = Cavaliere(input("Inserisci il nome del Cavaliere: "))
                    esercito.append(soldato)
                    budget -= soldato.get_costo()
                elif opzione == '2':
                    soldato = Arciere(input("Inserisci il nome dell'Arciere: "))
                    esercito.append(soldato)
                    budget -= soldato.get_costo()
                elif opzione == '3':
                    soldato = Mago(input("Inserisci il nome del Mago: "))
                    esercito.append(soldato)
                    budget -= soldato.get_costo()
                elif opzione == '4':
                    soldato = Guaritore(input("Inserisci il nome del Guaritore: "))
                    esercito.append(soldato)
                    budget -= soldato.get_costo()
                
                print(f"Hai speso {soldato.get_costo()} monete. Ti sono avanzati {budget} monete.")
                

        else:
            print("\n*** L'IA sta acquistando i soldati... ***")

            nuovo_esercito, budget = Esercito.genera_esercito_random([], budget)
            for soldato in nuovo_esercito:
                print(f"{soldato.get_nome()} ({type(soldato).__name__}) aggiunto all'esercito IA.")
            esercito.extend(nuovo_esercito) 
            time.sleep(2)

        return esercito, budget
