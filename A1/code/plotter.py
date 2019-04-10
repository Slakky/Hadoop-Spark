# import mapper

# import mapper.py
import matplotlib.pyplot as plt
import sys
import os
import json

x = []
y = []


def filter_retweets(tuits):
    return [tuit for tuit in tuits
            if 'retweeted_status' not in tuit]


def main():
    filepath = sys.argv[1]
    tuits = [json.loads(element)
             for element in sys.stdin
             if not element == "\n"]
    unique_tuits = len(filter_retweets(tuits))
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting ...".format(filepath))
        sys.exit()
    with open(filepath) as file:
        for line in file:
            line = line.strip()
            pronoun, freq = line.split(",")
            x.append(pronoun)
            y.append(int(freq) / int(unique_tuits))
    plt.bar(x, y, align='center')
    plt.xticks(x)
    plt.ylabel('Counts')
    plt.xlabel('Pronouns')
    plt.title('Pronoun count normalized Task 2')
    plt.savefig('pronounstuits.png')
    os.remove('unique_tuits.tmp')


if __name__ == '__main__':
    main()
