songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 12.2
paths = []

# set of every possible subset (s)
while len(paths) != (2**len(songs)):
    bob = []
    if bob not in paths:
        paths.append(bob)
    
    else:
        for n in songs:
            bob.append(n)
            if bob not in paths:
                None
            else:
                bob.pop()
        paths.append(bob)

npaths = []
for n in paths:
    our_size = 0
    for y in n:
        our_size += y[2]
    
    if our_size <= max_size:
        npaths.append(n)

last = ()
highest = 0
for c,n in enumerate(npaths):
    new = 0
    for k in n:
        new += k[1]
    
    if new > highest:
        last = npaths[c]
        highest = new

lastn = [n[0] for n in last]
print(lastn)