''' άσκηση από το http://pythonies.mysch.gr/chapters/answer.pdf

Στη Σελήνη το βάρος ενός αντικειμένου είναι το 1/6 του βάρους του στη
Γη. Στην Αφροδίτη το βάρος ενός αντικειμένου είναι 0,9 φορές το βάρος
του στη Γη. Στον Ήλιο το βάρος ενός αντικειμένου είναι 27,07 φορές το
βάρος του στη Γη, αλλά όταν βρίσκεται κανείς εκεί η αύξηση του βάρους
δεν είναι το βασικότερο πρόβλημα. Να γράψετε πρόγραμμα που θα ζητάει
από το χρήστη το βάρος του στη Γη και θα εμφανίζει το βάρος του στη
Σελήνη, την Αφροδίτη και τον Ήλιο.
'''

# Ας ξεκινήσουμε εξηγώντας στον χρήστη τι κάνει το πρόγραμμά μας
print("Πόσο θα ζυγίζαμε αν κατοικούσαμε σε κάποιο άλλο ουράνιο σώμα;")
print("Ανακάλυψέ το για τη Σελήνη, τον Ήλιο και τον πλανήτη Αφροδίτη.")

# ερώτηση για το βάρος και μετατροπή του από αλφαριθμητικό σε ακέραιο αριθμό
print("Πόσα κιλά είσαι;")
weight = int(input())

# υπολογισμός βάρους στα άλλα ουράνια σώματα, μετατροπή σε ακέραιο και
# αποθήκευση των αποτελεσμάτων σε κατάλληλες μεταβλητές
moon = int(weight/6)
sun = int(weight * 27.07)
venus = int(weight * 0.9)

# εμφάνιση των αποτελεσμάτων στην οθόνη
print("Το βάρος σου στη Γη είναι", weight, "κιλά.")
print("Το βάρος σου στη Σελήνη είναι", moon, "κιλά.")
print("Το βάρος σου στον Ήλιο είναι", sun, "κιλά.")
print("Το βάρος σου στην Αφροδίτη είναι", venus, "κιλά.")
