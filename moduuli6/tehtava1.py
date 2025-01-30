import random

def heitto():
    noppa = random.randint(1,6)
    return noppa
noppa = heitto()
print(noppa)

while noppa!=6:
    noppa = heitto()
    print(noppa)