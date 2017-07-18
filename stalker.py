import praw
from bs4 import BeautifulSoup
import requests

# Users to stalk (comma separated array)
stalk = ['stickano']

# You can define a specific Subreddit (default=all)
subreddit = 'all'

# True will insult the stalked individuals,
# False and it will compliment the users instead.
insult = True

# Define your Bot
client_id = ''
client_secret = ''
username = ''
password = ''

# The functionality - careful now!
bot = praw.Reddit(user_agent='stalkerBot v.1',
                  client_id=client_id,
                  client_secret=client_secret,
                  username=username,
                  password=password)

if insult is True:
    url = 'http://autoinsult.datahamster.com/?style=2'
    container = 'div'
    containerClass = 'insult'
else:
    url = 'http://www.complimentgenerator.co.uk/'
    container = 'p'
    containerClass = 'small'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')
fetchInsult = soup.find(container, {'class': containerClass})

botSignature = '\n\n &nbsp; \n\n Blip Blop I\'m the [StalkerBot!](https://github.com/Stickano/StalkerBot)'

sub = bot.subreddit(subreddit)
comments = sub.stream.comments()

for comment in comments:
    author = comment.author
    if author in stalk:
        # Thanks to u/Vaphell and u/ManyInterests for claification on string conversion.
        comment.reply(fetchInsult.text + botSignature)
