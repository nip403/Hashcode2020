from task1_setup import *

libraries.sort(key=lambda x: x.signup)
for l in libraries:
    #print([a.id for a in l.books])
    #bookids = list(set([m.id for m in l.books]))
    
    l.books.sort(key=lambda x: x.score, reverse=True)
    l.books = list(filter(lambda q: not q.scanned, l.books))

    for b in l.books:
        b.scanned = True

with open("set1.txt", "w+") as f:
    f.write(str(len(libraries))+"\n")
    for i in libraries:
        f.write(str(i.id) + " " + str(len(i.books))+"\n")
        f.write(" ".join([str(j.id) for j in i.books]) + "\n")