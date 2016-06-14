''' άσκηση από το από το http://pythonies.mysch.gr/chapters/planets.pdf

Τα μπισκότα τύχης (fortune cookies) είναι μπισκότα που στο εσωτερικό
τους περιέχουν μηνύματα με προβλέψεις γι’ αυτόν που τα ανοίγει. Υλο-
ποιήστε ένα πρόγραμμα που θα καλεί τον χρήστη να ανοίξει ένα τυχερό
μπισκότο και στη συνέχεια θα του εμφανίζει μια τυχαία πρόβλεψη.
'''

import random
import time

messages = [
"Η τύχη σου κρύβεται σε άλλο μπισκότο.",
"Ο καλύτερος τρόπος να παραμείνεις υγιής είναι να συνεχίσεις να τρως τυχερά μπισκότα.",
"Αποδέξου ότι κάποιες μέρες είσαι το περιστέρι και κάποιες άλλες το άγαλμα.",
"Μαθαίνεις από τα λάθη σου..., Σήμερα είναι μια μέρα που θα διδαχθείς πολλά.",
"Η σκληρή δουλειά θα σου ανταποδώσει στο μέλλον. Η τεμπελιά θα σου ανταποδώσει άμεσα...",
"Όλοι συμφωνούν: Είσαι ο καλύτερος!"
]

while True:
    print("Σήμερα είναι η τυχερή σου μέρα.")
    time.sleep(1)
    print("Θα σου κάνω μια πρόβλεψη για το μέλλον.")
    time.sleep(1)
    print("Έτοιμος; Πάτα <Enter> και η ζωή σου μπορεί να αλλάξει για πάντα!")
    input()
    print("Λοιπόν το τυχερό σου μπισκότο λέει...")
    time.sleep(1)
    # επιλογή τυχαίου μηνύματος από τη λίστα
    print(random.choice(messages))

    # ερώτηση για επανάληψη
    print("Θέλεις κι άλλο; (N/O)")
    answer = input().upper()
    if answer != 'Ν':
        break
