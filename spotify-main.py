#imports

import os
import json
import spotipy
import pandas
import spotipy.util as util
from json.decoder import JSONDecodeError

#hardcode the values for now
username = 'ryan_hoffman-us' #Change this to allow for username input
scope = 'user-read-private user-read-playback-state user-modify-playback-state' #Borrowed from iamsumat's code
client_id = '25e72c8800394165a1af4116a118836f' #change this so that it is hidden in a .gitignore
client_secret = 'b3286ac633c841c4b676ce46e73c2434' #change this so that it is hidden in a .gitignore

#retrieve access token
try:
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri='https://www.google.com/')
except (AttributeError, JSONDecodeError):
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri='https://www.google.com/')

sp = spotipy.Spotify(auth=token)

#Check to see that everything is working by printing user data
user = sp.current_user()
name = user['display_name'].split(' ')
print('%s spotify account' %(str(name[0])))

#Practice by retrieving all of the Talking Heads albums
query_url = 'https://api.spotify.com/v1/artists/' #?

#Retrieve the talking heads artist id