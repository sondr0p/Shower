# Import BeautifulSoup and Tweepy
from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import tweepy
import time
import datetime

# Get auth
auth = tweepy.OAuthHandler('consumerkey', 'consumersecret')
auth.set_access_token('token', 'tokensecret')

api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# Open connection and collect page
url = "https://www.reddit.com/r/Showerthoughts/top/"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# Parse page and print
page_soup = soup(page_html, 'html.parser')
container = page_soup.find('div', {'class':'top-matter'}) # Top Post
title = container.a.text
if len(title) < 140: # Check if string can be tweeted
    print(title) # Prints just the title
else:
    print('Tweet too long')

# Tweet top post
# api.update_status(title)
