# Jackie Chan (861158919)
# Abe Hu (861148832)
# Daniel Nguyen (861156246)




from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import ssl
import json
import os
import urllib.request as urllib2
from bs4 import BeautifulSoup
import requests

arguments = sys.argv[3:]
filename = sys.argv[1]
numtweets = int(sys.argv[2])

print(filename + " contains the tweets with a title attribute")
keywords = ' '.join(arguments)
print(keywords + " are the keywords")

#consumer key, consumer secret, access token, access secret.
ckey="5QVnDuXPag3EKOrjre2YRZNcm"
csecret="6k97AOJWD7vgtS2Ndq3sUmZWvUPBkMW1MXLI7L6nE7H8h4KsNJ"
atoken="815885741108494336-ooTId5Ha5QVsywP8TXOqSieZdBJE3Id"
asecret="nAuuwvhPwxbn5gMqJZgXuviMdPpxoeqgSxjmzWFPVEa2S"


class listener(StreamListener):
    counttweets = 0
    firstit = True
    arr = []
    def on_data(self, data):
        with open("originalstream.json", 'a') as the_file:
            if self.counttweets < numtweets:
                the_file.write(data)
                self.counttweets+=1
                print(self.counttweets)
            else:
                with open("originalstream.json", 'r') as the_file:
                    for line in the_file:
                        self.arr.append(json.loads(line))
                    for row in self.arr:
                        if not row['entities']['urls']:
                            print("No URLs in tweet")
                        else:
                            url = row['entities']['urls'][0]['url']
                            headers = {'User-Agent':'Mozilla/5.0'}
                            page = requests.get(url)
                            title = BeautifulSoup(page.text, "html.parser").title.string
                            # title = BeautifulSoup(urllib2.urlopen(row['entities']['urls'][0]['url']), "html.parser").title.string
                            row['title'] = title
                            print(row['title'])
                        with open(filename, 'a') as output:
                            output.write(json.dumps(row) + '\n')
                    sys.exit()
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=arguments)
