import praw
from praw.models import MoreComments
from urllib.parse import quote_plus
from datetime import datetime
from datetime import date
dt = date.today()



client_id = 'client_id here'
client_secret = 'client_secret here'
username = 'user here'
password = 'pw here'
user_agent = 'agent here'

# creating user instance
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     username=username,
                     password=password,
                     user_agent = user_agent)

btcCounts = 0
ethCounts = 0
dogeCounts = 0
dt = date.today()
dbtc = {}
deth = {}
ddoge = {}

phrase = 'bitcoin'
phrase1 = 'ethereum'
phrase2 = 'dogecoin'
phrase3 = 'crypto!stats'
subreddit = reddit.subreddit('all')
for comment in subreddit.stream.comments():
    if dt != date.today():
        dbtc[str(dt)] = btcCounts
        deth[str(dt)] = ethCounts
        ddoge[str(dt)] = dogeCounts
        with open('crypto_data', 'a') as convert_file:
            convert_file.write('\n\nBITCOIN: ')
            convert_file.write(json.dumps(dbtc))
            convert_file.write('\n\nETHEREUM: ')
            convert_file.write(json.dumps(deth))
            convert_file.write('\n\nDOGECOIN: ')
            convert_file.write(json.dumps(ddoge))
        btcCounts = 0
        ethCounts = 0
        dogeCounts = 0
        dt = date.today()
    lowerComment = comment.body.lower()

    if phrase in lowerComment:
        btcCounts += 1
        # print(f'btcCounts = {btcCounts}') # debug
        # print(lowerComment) # debug
    if phrase1 in lowerComment:
        ethCounts += 1
        # print(f'etcCounts = {ethCounts}') # debug
        # print(lowerComment) #debug
    if phrase2 in lowerComment:
        dogeCounts += 1
        # print(f'dogeCounts = {dogeCounts}') # debug
        # print(lowerComment) # debug
    if phrase3 in lowerComment:
        comment.reply(f'hello there! bitcoinbot here!\n\nbtc has been mentioned {btcCounts} times today\n\n'
              f'eth has been mentioned {ethCounts} times today\n\n'
              f'dogecoin has been mentioned {dogeCounts} times today\n\n'
              f'i hope this helps! summon me at any time by invoking crypto.stats, with a ! instead of a period!\n\n'
              f'my counter resets at midnight EST. have a great day!')