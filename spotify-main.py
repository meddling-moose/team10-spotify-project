import os
import spotipy
import pandas
import spotipy.util as util
from json.decoder import JSONDecodeError
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

def search_playlist(result, query): # returns the playlist id from the result of the search method
    if(str.lower(result['playlists']['items'][0]['name']) == str.lower(query) and
       result['playlists']['items'][0]['owner']['id'] == 'spotify'):
        playlist_id = result['playlists']['items'][0]['id']
        return playlist_id
    else:
        print('No playlist found for: ' + query)
        return None

#Create a list of countries
countries = ['France', 'Italy', 'Taiwan', 'Jamaica', 'Japan', 'USA', 'Mexico', 'Brazil', 'India', 
             'Australia', 'Nigeria', 'South Korea', 'Germany', 'United Kingdom', 'Spain', 'Colombia', 'Argentina',
             'Philippines', 'Dominican Republic', 'Guatemala', 'Chile', 'Puerto Rico', 'Peru', 'Turkey',
             'Greece', 'Vietnam', 'Sweden', 'Honduras', 'Costa Rica', 'Ecuador', 'Hong Kong', 'Netherlands',
             'El Salvador', 'Canada', 'Portugal', 'Venezuela', 'Ukraine', 'Paraguay', 'Bolivia', 'South Africa']
playlist_name = 'Top 50 - ' # + country

#Pull the 'Top 50 - <country name>' playlists for the countries in the list
for country in countries:
    search_result = sp.search(playlist_name + country, type='playlist', limit=1)
    playlist_id = search_playlist(search_result, playlist_name + country)
    if playlist_id is not None:
        playlist_tracks = sp.playlist_tracks(playlist_id, additional_types=('track'))
        track_ids = []
        track_names = []
        for track_obj in playlist_tracks['items']:
            #Get the track ids from the playlist and put it in a list      
            #Use the ids to search songs and their features/analysis and then put that data in csv files by country
            track_ids.append(track_obj['track']['id'])
            track_names.append(track_obj['track']['name'])
        #export dataframe to csv before the first for loop moves to next country
        track_information_df = pandas.DataFrame(sp.audio_features(track_ids))
        track_information_df.insert(0, 'name', track_names, False)
        #track_information_df.drop(['track_href', 'analysis_url'], axis=1) How do I do this?
        track_information_df.to_csv('resources/' + country + '.csv', sep=',', index=False, encoding='utf-8')
        print(f'Finished converting {country}\'s Top 50 Playlist to csv')