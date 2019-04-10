#!/usr/bin/python3

""" mapper.py """

import json
import sys
import string

pronouns = ('han', 'hon', 'den', 'det', 'denna', 'hen', 'denne')


def filter_retweets(tuits):
    return [tuit for tuit in tuits
            if 'retweeted_status' not in tuit]



def mapper(tuits):
    return print('\n'.join('{},{}'.format(word.lower(), 1)
                           for tuit in tuits
                           for word in tuit['text'].split()
                           if word.lower().translate(str.maketrans('','', string.punctuation))
                            in pronouns))

tuits = [json.loads(element)
         for element in sys.stdin
         if not element == "\n"]


filtered_tuits = filter_retweets(tuits)

mapper(filtered_tuits)
print('count,{}'.format(len(filtered_tuits)))
