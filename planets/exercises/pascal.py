''' άσκηση από το από το http://pythonies.mysch.gr/chapters/planets.pdf

Το τρίγωνο του Pascal είναι ένας τριγωνικός μαθηματικός πίνακας με
πολύ ενδιαφέρουσες ιδιότητες. Για να το κατασκευάσουμε, τοποθετούμε
αρχικά στην κορυφή του τριγώνου, δηλαδή στη γραμμή 0, τον αριθμό 1.
Kάθε αριθμός σε κάθε επόμενη γραμμή προκύπτει ως άθροισμα των δύο
αριθμών που βρίσκονται από πάνω του, εκτός από τον πρώτο και τον
τελευταίο αριθμό κάθε γραμμής που είναι πάντα το 1.

Από το τρίγωνο του Pascal μπορούμε να εξάγουμε τους τριγωνικούς αριθ-
μούς και τους αριθμούς Fibonacci, να υπολογίσουμε το ανάπτυγμα πο-
λυωνύμων ακόμα και να κατασκευάσουμε ένα φράκταλ που ονομάζεται
τρίγωνο Sierpinski.

Μια ιδιότητα του τριγώνου που θα χρησιμοποιήσουμε εμείς είναι η εξής:
ο αριθμός που βρίσκεται στη γραμμή n και στη στήλη y αντιστοιχεί στο
πλήθος των διαφορετικών τρόπων με τους οποίους μπορούμε να φέρουμε
y φορές κορώνα αν στρίψουμε ένα νόμισμα n φορές (θυμηθείτε ότι οι
γραμμές και οι στήλες αριθμούνται από το 0). Διαιρώντας αυτόν τον
αριθμό με το άθροισμα των αριθμών της γραμμής n, το οποίο είναι 2 εις
τη n, υπολογίζουμε την πιθανότητα να φέρουμε y φορές κορώνα αν στρίψουμε
ένα νόμισμα n φορές.

Να υλοποιήσετε ένα πρόγραμμα το οποίο διαβάζει το n από το χρήστη,
κατασκευάζει το τρίγωνο του Pascal μέχρι και τη γραμμή n και εμφανίζει,
για κάθε y, την πιθανότητα να φέρουμε y φορές κορώνα αν στρίψουμε
ένα νόμισμα n φορές.
'''

n = int(input("Πόσες φορές n θα στρίψουμε το νόμισμα; "))

# η πρώτη γραμμή
line = [1]
# για κάθε γραμμή, μέχρι τη n-οστή
for i in range(n):
    # πρώτο στοιχείο της νέας γραμμής
    newline = [1]
    # κάθε ενδιάμεσο στοιχείο της νέας γραμμής είναι...
    for index in range(1,len(line)):
        # το άθροισμα των δύο στοιχείων "από πάνω" του
        newline.append(line[index-1] + line[index])
    # τελευταίο στοιχείο της νέας γραμμής
    newline.append(1)
    line = newline
    # όλο το περιεχόμενο της for μπορεί να γραφτεί με μία μόνο γραμμή:
    # line = [1] + [line[index-1] + line[index] for index in range(1,len(line))] + [1]

# άθροισμα της n-οστής γραμμής
sum = 2 ** n    
# εμφάνιση πιθανοτήτων
print("Όταν στρίβεις ένα νόμισμα", n, "φορές, η πιθανότητα να φέρεις κορώνα:")
for times in range(0,n+1):
    print(times, "φορές:", line[times] / sum)

    
