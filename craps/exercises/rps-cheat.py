''' άσκηση από το http://pythonies.mysch.gr/chapters/craps.pdf

Να κατασκευάσετε ένα πρόγραμμα το οποίο θα παίζει το γνωστό παι-
χνίδι «Πέτρα-Ψαλίδι-Χαρτί» με το χρήστη. Σε κάθε γύρο, το πρόγραμμα
θα ζητά από το χρήστη την επιλογή του (1 για την Πέτρα, 2 για το Ψαλίδι
ή 3 για το Χαρτί) και στη συνέχεια θα εμφανίζει τη δική του επιλογή και
θα ανακοινώνει το νικητή του γύρου. Αν ο χρήστης πληκτρολογήσει οτι-
δήποτε εκτός από τις τρεις έγκυρες επιλογές τότε θεωρείται ότι επιθυμεί
να τερματίσει το παιχνίδι.

Στην παραλλαγή αυτή, το πρόγραμμα "κλέβει" με πιθανότητα 4 στις 5.
'''

import random
import time

# μετρητής των συνολικών παιχνιδιών
games = 0
# μετρητής των παιχνιδιών που κέρδισε ο παίκτης
wins = 0

print("Θα παίξουμε Πέτρα - Ψαλίδι - Χαρτί.")

while True:
    print("Δώσε την επιλογή σου. (1) Πέτρα, (2) Ψαλίδι, (3) Χαρτί ή οτιδήποτε άλλο για τερματισμό.")
    player = int(input())

    # αν ο παίκτης δώσει κάτι διαφορετικό εκτός από 1, 2 ή 3 τότε τερματίζουμε άμεσα την επανάληψη με break
    if player < 1 or player > 3:
        print("Αντίο!")
        break

    # η (όχι και τόσο τυχαία) επιλογή του προγράμματος
    # επιλέγεται ένας τυχαίος αριθμός από το 1 μέχρι το 100
    cheatprobability = random.randint(1,100)
    # αν τύχει να είναι το πολύ 20, τότε η επιλογή είναι τυχαία
    if cheatprobability <= 20:
        computer = random.randint(1,3)
    else:
        # ζαβολιά: επιλέγεται η κίνηση που κερδίζει την επιλογή του χρήστη (αίσχος)
        if player == 1:
            computer = 3
        elif player == 2:
            computer = 1
        else:
            computer = 2

    if computer == 1:
        print("O υπολογιστής διάλεξε Πέτρα.")
    elif computer == 2:
        print("O υπολογιστής διάλεξε Ψαλίδι.")
    else:
        print("O υπολογιστής διάλεξε Χαρτί.")

    # σύγκριση των επιλογών του παίκτη και του υπολογιστή και εμφάνιση κατάλληλου μηνύματος
    if computer == player:
        print("Ισοπαλία.")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("Κέρδισες!")
        wins = wins + 1
    else:
        print("Κέρδισε ο υπολογιστής :P")

    games = games + 1
    # εκτύπωσε 20 φορές τον χαρακτήρα "-"
    print(20 * "-")
    time.sleep(2)

print("Κέρδισες σε", wins, "από τα", games, "παιχνίδια.")
