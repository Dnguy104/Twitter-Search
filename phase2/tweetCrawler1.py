#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#import other utilites
import sys
import re
import threading
import urllib2
from bs4 import BeautifulSoup
import sys
import os
import requests
import ssl
import json


consumer_key = "5QVnDuXPag3EKOrjre2YRZNcm"
consumer_secret = "6k97AOJWD7vgtS2Ndq3sUmZWvUPBkMW1MXLI7L6nE7H8h4KsNJ"

access_token = "815885741108494336-ooTId5Ha5QVsywP8TXOqSieZdBJE3Id"
access_token_secret = "nAuuwvhPwxbn5gMqJZgXuviMdPpxoeqgSxjmzWFPVEa2S"

counter = 0
file_name = "data/tweets" + str(counter) + ".json"

while os.path.exists(file_name) :	
	counter += 1
	file_name = "data/tweets" + str(counter) + ".json"

f = ""
t1 = ""
lock = threading.Lock()

 
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)


def loookUpLink(match, data):

    if data is None:
        return

    link = match.group(0).replace("\\" , "")    
    print link
    page = requests.get(link)
    title = BeautifulSoup(page.text, "html.parser").title.string


    appendTitle(title, data)

def appendTitle(title, data):

    if "\"geo_enabled\":false" in data:
        return

    if  "{\"limit\":" in data:
        return

    global f
    d = json.loads(data);

    d['title'] = title;
    lock.acquire() # thread blocks at this line until it can obtain lock
    
    try:
        f.write(json.dumps(d) + '\n')

    except Exception, e:
        f.write(data)


    #f.write('\n')
    lock.release()


    # Example usage
def printTweet(data):
    #check data here!
    #run all strings inside .html checker
    global t1
    listTokens = data.split("\"")
    title = ""
    foundTitle = False

    for s in listTokens:
        match = re.search(r'(https|http).*(\.html|\.htm)', s)
      
        if match:
            #pass data into thread for lookup
            t1 = FuncThread(loookUpLink, match, data)
            t1.start()
            foundTitle = True
            break


    if foundTitle is False:
        appendTitle(title, data)


class StdOutListener(StreamListener):

    def on_data(self, data):

        global file_name 
        global f
        global t1
        statinfo = os.stat(file_name)

        #if file is > 10MB
        if(statinfo.st_size >= 10000000): 
            
            #if t1 is alive, wait for t1 to finish printing our url title and then close
            if t1.is_alive():
                t1.join()

            f.close()
            global counter
            #open new file 
            file_name = "data/tweets" + str(counter) + ".json"
            


            f = open(file_name, 'w')
            #print "opened file: " + file_name
            counter+= 1


        printTweet(data)
        return True

    def on_error(self, status_code):
		#print "Error: " + repr(status_code)
		return True # False to stop

    def on_limit(self, track):
    	#print "!!! Limitation notice received: %s" % str(track)
    	return

	# def on_timeout(self):
	# 	print 'Timeout... Quitting'
	# 	return True


if __name__ == '__main__':

    print 'Starting....'

    #FILL TEXT FILE WITH TWEETS
    orig_stdout = sys.stdout
    global file_name
    global f
    f = open(file_name, 'w')

    print "Starting"

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Filter for all tweets in all locations of the globe
    stream.filter(locations=[-180,-90,180,90])
    # stream.filter(track=['python', 'javascript', 'ruby'])


    sys.stdout = orig_stdout
    f.close()

    print 'Closed!....'


