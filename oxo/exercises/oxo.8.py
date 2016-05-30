""" επέκταση του http://pythonies.mysch.gr/chapters/oxo.pdf

Η συνάρτηση readPosition ξεκινά εμφανίζοντας στον παίκτη την
τρέχουσα κατάσταση του πίνακα του παιχνιδιού:

# εμφάνιση πίνακα τρίλιζας και πιθανών κινήσεων
print3x3(board)
print3x3(range(9))

Αντικαταστήστε την τελευταία από τις εντολές, όπως φαίνεται στον 
κώδικα που ακολουθεί:

# εμφάνιση πίνακα τρίλιζας και πιθανών κινήσεων
print3x3(board)
p = [position if board[position] == " " else "."
     for position in range(9)]
print3x3(p)

Εκτελέστε το πρόγραμμα και παρατηρήστε τι συμβαίνει. Τί ακριβώς 
περιέχει η λίστα p;

Απάντηση: Κάθε στοιχείο της λίστας p περιέχει είτε τον αριθμό 
μιας θέσης, εφόσον αυτή είναι διαθέσιμη, είτε ένα κενό. 
Χρησιμοποιώντας την print3x3 με παράμετρο αυτή τη λίστα p, 
εμφανίζονται στο χρήστη οι αριθμοί των διαθέσιμων θέσεων,
όπως αυτοί αντιστοιχούν στα τετράγωνα της τρίλιζας.
"""

import random

def print3x3(board, trailing = True):
    """ Εμφανίζει σε διάταξη 3x3 τα περιεχόμενα
        μιας λίστας με 9 (τουλάχιστον) στοιχεία.
        board: Λίστα που θα εμφανιστεί σε διάταξη 3χ3
    """
    print(" ", board[0], "|", board[1], "|", board[2])
    print(" ---+---+---")
    print(" ", board[3], "|", board[4], "|", board[5])
    print(" ---+---+---")
    print(" ", board[6], "|", board[7], "|", board[8])
    if trailing:
        print()

def readPosition(player, board):
    """ Διαβάζει από τον παίκτη τη θέση
        στην οποία επιθυμεί να παίξει και την
        επιστρέφει.
        player: Ο παίκτης που έχει σειρά να παίξει
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)
    """
    # εμφάνιση πίνακα τρίλιζας και πιθανών κινήσεων
    print3x3(board)
    p = [position if board[position] == " " else "." 
         for position in range(9)]
    print3x3(p)
    # επανάληψη: όσο το τετράγωνο δεν είναι έγκυρο
    while True:
        # επιλογή θέσης από τον παίκτη
        print(player, "διάλεξε τετράγωνο:", end=" ")
        position = int(input())
        # έλεγχος εγκυρότητας
        if position < 0 or position > 8:
            print("Επίλεξε τιμή μεταξύ 0 και 8.")
        elif board[position] != " ":
            print("To", position, "δεν είναι κενό.")
        else:
            # έγκυρη τιμή, τέλος επανάληψης
            break
    # επιστροφή επιλεγμένης θέσης
    return position

def play(player, pos, board):
    """ Πραγματοποιεί και ανακοινώνει την κίνηση
        ενός παίκτη σε συγκεκριμένη θέση
        player: Το σύμβολο του παίκτη
        pos: Η θέση στην οποία παίζει ο παίκτης
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)        
    """
    # ανακοίνωση κίνησης
    print("Ο παίκτης", player, "παίζει στο", pos)
    # συμπλήρωση επιλεγμένης θέσης
    board[pos] = player

def check(player, board):
    """ Ελέγχει αν υπάρχει 3άδα όπου ο παίκτης player
        έχει καταλάβει και τις 3 θέσεις.
        player: σύμβολο παίκτη ("Χ" ή "Ο")
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)    
    """
    # για κάθε 3άδα θέσεων
    for triple in triples:
        # p1, p2 και p3 οι τρεις θέσεις της 3άδας
        p1, p2, p3 = triple
        # αν ο παίκτης έχει καταλάβει και τις 3 θέσεις
        if board[p1] == board[p2] == board[p3] == player:
            return True
    # αν φτάσουμε μέχρι εδώ, ο έλεγχος απέτυχε
    return False

def checkPartial(player, board):
    """ Ελέγχει αν υπάρχει 3άδα όπου ο παίκτης player
        έχει καταλάβει τις 2 από τις τρεις θέσεις.
        Επιστρέφει την 3η κενή θέση της 3άδας ή None.
        player: σύμβολο παίκτη ("Χ" ή "Ο")
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)    
    """
    # για κάθε 3άδα θέσεων
    for triple in triples:
        # p1, p2 και p3 οι τρεις θέσεις της 3άδας
        p1, p2, p3 = triple
        # αν ο παίκτης έχει καταλάβει τις 2 από τις 3 θέσεις
        if board[p1] == " " and board[p2] == board[p3] == player:
            return p1
        elif board[p2] == " " and board[p1] == board[p3] == player:
            return p2
        elif board[p3] == " " and board[p1] == board[p2] == player:
            return p3
    # αν φτάσουμε μέχρι εδώ, ο έλεγχος απέτυχε
    return None

def next(player):
    """ Επιστρέφει το σύμβολο του παίκτη που παίζει
        μετά τον παίκτη με σύμβολο player.
        player: σύμβολο παίκτη ("Χ" ή "Ο")
    """
    if player == "X":
        return "O"
    else:
        return "X"

def available(board):
    """ Επιστρέφει μια λίστα με τις διαθέσιμες θέσεις
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)    
    """
    return [s for s in range(9) if board[s] == " "]

def paperPosition(board):
    """ Επιστρέφει τον αριθμό της θέσης όπου πρέπει
        να παίξει ο Χ, σύμφωνα με το "έξυπνο χαρτί".
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)    
    """
    # πόσες κινήσεις έχει κάνει ο Χ;
    nbMoves = board.count("X")
    if nbMoves == 0:
        # κίνηση 1η: πάνω αριστερά γωνία (θέση 0)
        return 0
    elif nbMoves == 1:
        # κίνηση 2η: κάτω δεξιά γωνία (θέση 8), αν
        # είναι διαθέσιμη, αλλιώς πάνω δεξιά (θέση 2)
        if board[8] == " ":
            return 8
        else:
            return 2
    elif nbMoves < 4:
        # κίνηση 3η, 4η: αν ο "X" κάνει τρίλιζα
        position = checkPartial("X", board)
        if position is not None:
            return position
        # έλεγξε αν ο "Ο" μπορεί να κάνει τρίλιζα
        position = checkPartial("O", board)
        if position is not None:
            return position
        # αλλιώς παίξε σε οποιαδήποτε ελεύθερη γωνία
        for corner in (0,2,6,8):
            if board[corner] == " ":
                return corner
    else:
        # κίνηση 5η: παίξε στο διαθέσιμο τετράγωνο
        return board.index(" ")


# οι 3άδες των θέσεων που σχηματίζουν τρίλιζες
triples = (
    (0,1,2),(3,4,5),(6,7,8),    # οριζόντια
    (0,3,6),(1,4,7),(2,5,8),    # κάθετα
    (0,4,8),(2,4,6))            # διαγώνια
# η αναπαράσταση της τρίλιζας: 
# μια λίστα με 9 χαρακτήρες (" ", "Χ" ή "Ο")
# αρχικά, όλα τα τετράγωνα είναι κενά
board = 9 * [" "]
# ο παίκτης που θα παίξει πρώτος
player = "X"
# ο παίκτης που θα κατευθύνεται από το πρόγραμμα
computer = "X"
# πλήθος τετραγώνων που απομένουν κενά
blank = 9
# λογική μεταβλητή που δείχνει αν έχει γίνει τρίλιζα
inarow = False
# επανάληψη: συνεχίζεται όσο υπάρχουν κενά τετράγωνα
#   και δεν έχει γίνει τρίλιζα
while blank > 0 and not inarow:
    if player == computer:
        # επιλογή θέσης από το πρόγραμμα
        position = paperPosition(board)
    else:
        # επιλογή θέσης από τον παίκτη
        position = readPosition(player, board)
    # συμπλήρωση επιλεγμένης θέσης
    play(player, position, board)
    # μείωση κενών τετραγώνων κατά 1
    blank -= 1
    # έλεγχος για τρίλιζα
    inarow = check(player, board)
    # εναλλαγή παίκτη
    player = next(player)
# εμφάνιση τελικού πίνακα τρίλιζας
print3x3(board)
# εμφάνιση αποτελέσματος
if inarow:
    print("Τρίλιζα! Κέρδισε ο", next(player))
else:
    print("Ισοπαλία.")
