# Python script to plot chatacter frequencies

import matplotlib.pyplot as plt
import sys
import os

x = []
y = []

def main():
    filepath = sys.argv[1]


    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting ...".format(filepath))
        sys.exit()
    with open(filepath) as file:
        for line in file:
            line = line.strip()
            char = line.split(",")[0]
            freq = line.split(",")[1]
            if char.isalpha():
                x.append(char)
                y.append(int(freq))
    plt.bar(x, y, align = 'center')
    plt.xticks(x)
    plt.ylabel('Frequency')
    plt.xlabel('Characters')
    plt.title('Character frequency Task 1.4')
    plt.savefig('frequencyplot.png')
if __name__ == '__main__':
    main()
