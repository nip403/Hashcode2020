#task1_example.py
from task1_setup import *

l = libraries[0]
l.books.sort(key=lambda x: x.score, reverse=True)

efficiencies = []

score = 0
days = l.signup
n = 0
while n+1 < len(l.books):
    score += int(l.books[n].score)
    score += int(l.books[n+1].score)
    n += 2
    days += 1
    efficiencies.append(score/days)

print(efficiencies)
