to_read = "a_example.txt"

global_books = []
libraries = []

class book:
    def __init__(self,id,score):
        self.id,self.score=id,score
        self.scanned = False

    def __lt__(self, b):
        return self.score < b.score

    def __gt__(self, b):
        return self.score > b.score

    def __eq__(self, b):
        return self.score == b.score


class library:
    def __init__(self,signup,booksperday):
        self.signup,self.booksperday = signup,booksperday
        self.books = []

f = open(to_read,"r")
lines = f.readlines()

for id,score in enumerate(lines[1].split()):
    global_books.append(book(id,score))

n = 2
_id = 0
while n < len(lines):
    this_library = lines[n:n+2]
    parms = this_library[0].split()
    libraries.append(library(int(parms[1]),int(parms[2])))
    for i in this_library[1].split():
        libraries[-1].books.append(global_books[int(i)])

    libraries[-1].id = _id
    _id += 1
    n += 2
