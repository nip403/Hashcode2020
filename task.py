import sys
to_read = sys.argv[1]
out = sys.argv[2]

books = []
scanned = {}
libraries = []
7
class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False

    def __lt__(self, b):
        return self.score < b.score

    def __gt__(self, b):
        return self.score > b.score

    def __eq__(self, b):
        return self.score == b.score

f = open(to_read,"r")
lines = f.readlines()

for id, score in enumerate(lines[1].split()):
    books.append(Book(id, score))

B, L, D = list(map(int, lines[0].split(" ")))

class Library:
    def __init__(self, id, signup, booksperday, books):
        self.id = id
        self.signup = signup
        self.booksperday = booksperday
        self.books = books
        self.books.sort()
        self.books = self.books[::-1]
        self.estimate = sum([int(b.score) for b in self.books[:(D-1-self.signup)//self.booksperday]])

    def __lt__(self, b):
        return self.estimate < b.estimate

    def __gt__(self, b):
        return self.estimate > b.estimate

    def __eq__(self, b):
        return self.estimate == b.estimate



i = 0
for n in range(2, len(lines), 2):
    l = lines[n: n + 2]
    N, T, M = list(map(int, l[0].strip().split(" ")))
    books_available = list(map(int, l[1].split(" ")))
    libraries.append(Library(i, T, M, list(map(lambda i: books[i], books_available))))
    i += 1

libraries.sort()
best_library = libraries.pop(0)

days_left = D

decisions = []

while days_left > 0 and days_left >= best_library.signup and len(libraries) >= 0:
    best_library.books = list(filter(lambda x: not x.scanned, best_library.books))
    books_that_can_be_scanned = min((days_left - best_library.signup) * best_library.booksperday, len(best_library.books))
    l1 = str(best_library.id) + " " + str(books_that_can_be_scanned)

    ids_to_scan = []

    for j in range(books_that_can_be_scanned):
        ids_to_scan.append(best_library.books[j].id) 
        best_library.books[j].scanned = True

    l2 = " ".join(map(str, ids_to_scan))

    decisions.append([l1, l2])

    days_left -= best_library.signup
    try:
        best_library = libraries.pop(0)
    except:
        continue

with open(out, "w") as f:
    f.write(str(len(decisions)) + "\n")

    for decision in decisions:
        f.write(decision[0] + "\n")
        f.write(decision[1] + "\n")

