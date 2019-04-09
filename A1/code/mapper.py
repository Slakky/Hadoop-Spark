import json
import sys


#[f(x) if condition else g(x) for x in sequence]
#[pair for pair in enumerate(mylist)]
#[f(x) for x in sequence if condition]

tuits = [(counter,line)\
	for counter,line in enumerate(sys.stdin)\
        if not line == "\n"]

for i in range(len(tuits)):
    tuit = json.loads(tuits[i][1])
    print(tuit)
#for counter, line in enumerate(sys.stdin.strip()):
#    print(counter, line)
#    if not line == "\n":
#        tuits = json.loads(line)
#    else:
#        pass
#print(counter)
