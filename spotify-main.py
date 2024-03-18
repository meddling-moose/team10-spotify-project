#imports

import os
import json
import spotipy
import pandas
import spotipy.util as util
from json.decoder import JSONDecodeError
import requests
#from config import username
#from config import client_id
#from config import client_secret

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
talking_heads = '2x9SpqnPi8rlE9pjHBwmSC'
anri_uri = 'spotify:artist:0xGtOrmB2hnrNRLG3vhpSo'

#Retrieve the talking heads artist id, anri artist id
#Anri - https://open.spotify.com/artist/0xGtOrmB2hnrNRLG3vhpSo?si=AqFjbL0fSGuahy7mZNQVww
#Talking Heads - https://open.spotify.com/artist/2x9SpqnPi8rlE9pjHBwmSC?si=4I0U_j3sRmqmJ3FnugreZQ

results = sp.artist_albums(anri_uri, album_type='album')
anris_albums = results['items']

while results['next']: #Stole this from stack overflow, but it's also in the spotipy get started page
    results = sp.next(results)
    anris_albums.extend(results['items'])

print('-- Anris Spotify Album Data --')
for album in anris_albums:
    print('-~-~-')
    print('Album Name: ' + album['name'])
    print('Album ID: ' + album['id'])
    print('Album Release Year: ' + album['release_date'])
    print('Number of tracks: ' + str(album['total_tracks']))
print('END OF LIST')

sp.artist(anri_uri)
timely = sp.album('spotify:album:2X9EFWmSWAYLjKm9y6llqL') # https://open.spotify.com/album/2X9EFWmSWAYLjKm9y6llqL?si=YXWQpU8LQRSVg4hCcsnj6Q
#print(timely)