from esercito import Esercito
import time


esercito = Esercito()
esercito_giocatore, budget_giocatore = esercito.crea_esercito()
esercito_ia = []
esercito_ia, budget_ia = Esercito.genera_esercito_random(esercito_ia, budget=1000)

round_num = 1

while esercito_giocatore and esercito_ia:
    print(f"Composizione Esercito Giocatore: ")
    for soldato in esercito_giocatore:
        print(f"- {soldato.get_nome()} ({type(soldato).__name__})")
    print(f"Budget rimanente del Giocatore: {budget_giocatore}")

    print(f"Composizione Esercito IA: ")
    for soldato in esercito_ia:
        print(f"- {soldato.get_nome()} ({type(soldato).__name__})")
    print(f"Budget rimanente dell' IA: {budget_ia}")


    print(f"\n=== ROUND {round_num} ===")
    esercito_giocatore, esercito_ia = Esercito.esegui_round(esercito_giocatore, esercito_ia)

    budget_giocatore += 50
    budget_ia += 50
    print("\n--- Fine Round ---")
    time.sleep(3)

    print(f"\nBudget Giocatore: {budget_giocatore}, Budget IA: {budget_ia}")
    esercito_giocatore, budget_giocatore = Esercito.acquista_soldati(esercito_giocatore, budget_giocatore, True)
    esercito_ia, budget_ia = Esercito.acquista_soldati(esercito_ia, budget_ia, False)
    round_num += 1

# QUI ARRIVA QUANDO UNO DEI DUE Eserciti è VUOTO
if esercito_giocatore:
    vincitore = "Giocatore"
else:
    vincitore = "IA"

print(f"\nVittoria di {vincitore} in {round_num - 1} round!")
print(f"Soldati rimasti: {len(esercito_giocatore) if esercito_giocatore else len(esercito_ia)}")


