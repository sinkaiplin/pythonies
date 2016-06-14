''' άσκηση από το από το http://pythonies.mysch.gr/chapters/planets.pdf

Στο τυχερό παιχνίδι Λοττο, ο παίκτης επιλέγει έξι αριθμούς από το 1
μέχρι και το 49. Στη συνέχεια κληρώνονται έξι αριθμοί με τυχαίο τρόπο.
Ανάλογα με το πλήθος των αριθμών που κατάφερε να μαντέψει ο παίκτης,
έχει και τα αντίστοιχα κέρδη.

Να υλοποιήσετε πρόγραμμα που θα ζητάει από τον χρήστη τους έξι αριθ-
μούς της επιλογής του. Στη συνέχεια θα παράγει τους έξι τυχερούς αριθ-
μούς που κληρώνονται. Θα πρέπει να εξασφαλίζεται ότι δεν εμφανίζεται
πολλές φορές ο ίδιος αριθμός είτε στην εξάδα των τυχερών αριθμών είτε
στην εξάδα των αριθμών που επιλέγει ο παίκτης. Το πρόγραμμα θα εμ-
φανίζει στον παίκτη τους αριθμούς που επέλεξε, τους τυχερούς αριθμούς
και πόσους από τους τυχερούς αριθμούς πέτυχε σωστά.

Καλό είναι να υλοποιήσετε τις επιμέρους λειτουργίες του προγράμματος
με συναρτήσεις. Θα μπορούσατε να υλοποιήσετε τις εξής:
- inputNumbers() που διαβάζει από το χρήστη 6 αριθμούς, εξασφα-
λίζοντας ότι βρίσκονται μεταξύ 1 και 49 και δεν επαναλαμβάνονται,
και τους επιστρέφει σε μια λίστα.
- generateNumbers() που δημιουργεί 6 τυχαίους αριθμούς μεταξύ 1
και 49, εξασφαλίζοντας ότι δεν επαναλαμβάνονται, και τους επι-
στρέφει σε μια λίστα.
- compare() που δέχεται σαν παραμέτρους δύο λίστες και επιστρέφει
μια λίστα με τα στοιχεία που βρίσκονται και στις δύο. Εναλλακτικά,
θα μπορούσε να επιστρέφει απλά το πλήθος αυτών των στοιχείων.
'''

import random

def inputNumbers():
    """ Διαβάζει 6 μοναδικούς αριθμούς από το χρήστη
        και τους επιστρέφει σε λίστα
    """
    numbers = []
    counter = 0
    # για κάθε έναν από τους 6 αριθμούς, επανάληψη:
    while counter < 6:
        # είσοδος αριθμού
        print(counter+1, "-- Επίλεξε έναν αριθμό από το 1 μέχρι και το 49")
        number = int(input())
        # έλεγχος αριθμού
        if number < 1 or number > 49:
            print("Αριθμός εκτός ορίων.")
        elif number in numbers:
            print("Αριθμός ήδη επιλεγμένος.")
        else:
            # προσθήκη αριθμού στη λίστα
            numbers.append(number)
            counter = counter + 1
    # επιστροφή λίστας αριθμών
    return numbers

def generateNumbers():
    """ Δημιουργεί 6 τυχαίους μοναδικούς αριθμούς
        και τους επιστρέφει σε λίστα
    """
    # μια λίστα με όλους τους αριθμούς από το 1 μέχρι και το 49
    numbers = [number for number in range(1,50)]
    counter = 0
    # για κάθε έναν από τους 6 αριθμούς, επανάληψη:
    while counter < 6:
        # τυχαία επιλογή της *θέσης* του αριθμού στη λίστα numbers
        # εξαιρούνται οι counter πρώτες θέσεις της λίστας
        index = random.randint(counter,48)
        # αντιμετάθεση του αριθμού που επιλέχθηκε
        # με τον αριθμό στη θέση counter
        numbers[index], numbers[counter] = numbers[counter], numbers[index]
        counter = counter + 1
    # επιστροφή λίστας αριθμών
    return numbers[:6]

def compareNumbers(list1, list2):
    """ Επιστρέφει το πλήθος των κοινών στοιχείων ανάμεσα σε δύο λίστες
    """
    equal = 0
    for number in list1:
        if number in list2:
            equal += 1
    return equal

# είσοδος αριθμών από το χρήστη
userNumbers = inputNumbers()
# κλήρωση τυχερών αριθμών
luckyNumbers = generateNumbers()

# εμφάνιση αριθμών
print("Οι αριθμοί που επιλέξατε: ", sorted(userNumbers))
print("Οι αριθμοί που κληρώθηκαν: ", sorted(luckyNumbers))
# σύγκριση εξάδων και ανακοίνωση αποτελεσμάτων
hits = compareNumbers(userNumbers, luckyNumbers)
if hits == 0:
    print("Δεν πετύχατε κανέναν αριθμό.")
elif hits == 1:
    print("Πετύχατε έναν αριθμό.")
else:
    print("Πετύχατε ", hits, "αριθμούς.")
