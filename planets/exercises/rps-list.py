﻿import random
import time

choices = ["Πέτρα", "Ψαλίδι", "Χαρτί"]

# μετρητής των συνολικών παιχνιδιών
games = 0
# μετρητής των παιχνιδιών που κέρδισε ο παίκτης
wins = 0

print("Θα παίξουμε Πέτρα - Ψαλίδι - Χαρτί.")

while True:

    print("Δώσε την επιλογή σου: (1) Πέτρα, (2) Ψαλίδι, (3) Χαρτί ή οτιδήποτε άλλο για τερματισμό.")
    player = int(input())

    # αν ο παίκτης δώσει άλλο γράμμα εκτός από Π, Ψ ή Χ τότε τερματίζουμε άμεσα την επανάληψη με break
    if player < 1 or player > 3:
        print("Αντίο!")
        break

    player = player-1
    print("Διάλεξες", choices[player])

    # η (τυχαία) επιλογή του προγράμματος
    computer = random.randint(0,2)
    print("O υπολογιστής διάλεξε", choices[computer])

    # σύγκριση των επιλογών του παίκτη και του υπολογιστή και εμφάνιση κατάλληλου μηνύματος
    if computer == player:
        print("Ισοπαλία.")
    elif computer == (player + 1) % 3:
    # elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("Κέρδισες!")
        wins = wins + 1
    else:
        print("Κέρδισε ο υπολογιστής :P")

    games = games + 1
    # εκτύπωσε 20 φορές τον χαρακτήρα "-"
    print(20 * "-")
    time.sleep(2)

print("Κέρδισες σε", wins, "από τα", games, "παιχνίδια.")
