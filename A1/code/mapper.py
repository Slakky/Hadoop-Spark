
""" mapper.py """

import json
import sys

pronouns = ('han', 'hon', 'den', 'det', 'denna', 'hen')


def filter_retweets(tuits):
    return [tuit for tuit in tuits
            if 'retweeted_status' not in tuit]


def mapper(tuits):
    return print('\n'.join('{}\t{}'.format(word, 1)
                           for tuit in tuits
                           for word in tuit['text'].split()
                           if word in pronouns))


tuits = [json.loads(element)
         for element in sys.stdin
         if not element == "\n"]

filtered_tuits = filter_retweets(tuits)

mapper(filtered_tuits)
