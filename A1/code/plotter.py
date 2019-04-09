# import mapper


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
            pronoun, freq = line.split(",")
            x.append(pronoun)
            y.append(int(freq))
    plt.bar(x, y, align='center')
    plt.xticks(x)
    plt.ylabel('Counts')
    plt.xlabel('Pronouns')
    plt.title('Pronoun count normalized Task 2')
    plt.savefig('pronounstuits.png')


if __name__ == '__main__':
    main()
