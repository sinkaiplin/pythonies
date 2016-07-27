''' επέκταση από το http://pythonies.mysch.gr/chapters/answer.pdf

Να τροποποιήσετε το πρόγραμμα του Deep Thought έτσι ώστε να ρωτάει το χρήστη για την Απάντηση, αντί να την ανακοινώνει απευθείας. Το πρόγραμμα θα ελέγχει αν ο χρήστης πράγματι γνωρίζει την Απάντηση και θα του εμφανίζει ανάλογο μήνυμα.

Nα επεκτείνετε το πρόγραμμά σας έτσι ώστε να δίνεται μια δεύτερη ευκαιρία στο χρήστη, αν αυτός δεν γνωρίζει την Απάντηση. Πιθανώς, πριν ο χρήστης ερωτηθεί για δεύτερη φορά, το πρόγραμμα θα μπορούσε να του εμφανίζει κάποια υπόδειξη.
'''

# είσοδος ονόματος
print("Πώς σε λένε;")
name = input()

# ορισμός της Απάντησης
answer = "42"

# ο χρήστης ερωτάται για την Απάντηση
print("Λοιπόν", name, "ποια είναι η Απάντηση;")
reply = input()

# έλεγχος της Απάντησης του χρήστη
if reply == answer:
    print("Αααα, είσαι μυημένος...")
else:
    print("Έλα, θα σε βοηθήσω.")
    print("Είναι ο τέταρτος κατά σειρά θετικός ακέραιος", end=" ")
    print("που αριστερά και δεξιά του έχει πρώτους αριθμούς.")
    print("Τώρα", name, "ξέρεις την Απάντηση;")
    reply = input()
    if reply == answer:
        print("Μπράβο, πολύ καλύτερα...")
    else:
        print("Άστο καλύτερα.")
