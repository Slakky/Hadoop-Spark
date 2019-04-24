# import mapper

# import mapper.py
import matplotlib.pyplot as plt
import sys
import os
import json

x = []
y = []

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting ...".format(filepath))
    sys.exit()
with open(filepath) as file:
    for line in file:
        line = line.strip()
        pronoun, freq = line.split(",")
        x.append(pronoun)
        y.append(int(freq))

unique_tuits = y[-1]
normalized_frequencies = [x / unique_tuits for x in y[1:]]

plt.bar(x[1:], normalized_frequencies, align='center')
plt.xticks(x[1:])
plt.ylabel(' Normalized Counts')
plt.xlabel('Pronouns')
plt.title('Task 2')
plt.savefig('pronounstuits.png')
