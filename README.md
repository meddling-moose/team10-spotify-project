
![image](https://github.com/meddling-moose/team10-spotify-project/assets/157430192/bdd3a332-a4d6-4ba3-948a-733deed7a618)
# About the Project
Spotify (/ˈspɒtɪfaɪ/; Swedish: [ˈspɔ̂tːɪfaj]) is a Swedish[6] audio streaming and media service provider founded on 23 April 2006.[7] It is one of the largest music streaming service providers, with over 602 million monthly active users, including 236 million paying subscribers, as of December 2023.
Spotify is available in most of Europe, as well as Africa, the Americas, Asia, and Oceania, with a total availability in 184 markets.[9] Its users and subscribers are based largely in the US and Europe, jointly accounting for around 53% of users and 67% of revenue.[10] It has no presence in mainland China where the market is dominated by QQ Music. 
Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform. Full Spotipy / Spotify Web API (Spotify offers multiple APIs, for our project we used the Web API) documentation available here: https://developer.spotify.com/documentation/web-api
•	Here, we have explored and examined musical attributes globally
•	Conducted data cleaning to perform exploratory data analysis (EDA) and data visualization of the Spotify dataset using Python (Pandas, NumPy, Matplotlib, Scipy.stats).
•	Data analysis - Analyzed attributes like “danceability” and “energy”.  We could not analyze song, artist popularity by country, genre, etc. (i.e. our original goal)
# Technical challenges:
1. API often did not provide the data in the format, or in its content, to support our analyses (i.e. forced to focus on aggregated music attributes, rather      than their popularity by country and artist as we desired.
2. Spotify token process to access API (different, more indirect process than web api calls for NYT or OpenWeather taught in class) required learning and implementing a new api call process using tokens
3. Installing Spotipy library in order to access Spotify API 
4. Modifying Mac/Win shell to store Spotify credentials to anonymize code (not taught)
# The Approach:
1. We set up Spotipy wrapper library with client id and client secret credentials.
2. Setup Spotipy account with token access
3. Created client id and client secret and retrieved the access token
4. Combined CSVs and calculate averages for audio features by country
5. DATA CLEAN UP
Combined country data files into one combined dataframe "df_combined" for analysis
- Use the Argentina.csv playlist as a sample to create a list of columns that are numerical (floats or ints) since statistical anaylsis can only be done on numerical data. This list of columns is then used to both calculate  averages and then to be listed as the keys of the master dataframe that will combine the averages of every column for every country.
- Iterated through every CSV created in the prior cell to calculate the average of each column (i.e. audio feature) for each CSV then add it to a master dictionary of all the averages that will later be converted into a dataframe.
- Used the os.listdir() method to get the list of all files in the resources directory
- Removed file extension to use the name as the country for the dataframe at the end
- Concatenated the name of the file with the name of the folder it is inside of (e.g. 'resources/Argentina.csv')
- Converted the dictionary created above into a dataframe
- Set the country as the index to make it easier to later find the minumum and maximum values/countries
- Displayed country name as country codes are available in Spotipy API.  
  Online we found a dictionary that mapped country name to country code. We then swapped the keys and values to make a new dictionary to map country codes to countries since the Spotify API provided a list of country codes where Spotify was available. But we needed to convert those codes to country names so we can later find the top 50 playlist for each country.
- There was also some additional data cleaning that is referenced under #14 
6. Compared Acousticness vs. Loudness globally
- Calculate correlation coeeficient using Pearson's R correlation method
7. Used central database to run a linear regression across countries, visualize negative correlation/regression results. 
- Finding: The more acoustic an album is the less loud it tends to be
8. Compared Acousticness vs. Loudness globally
- Define a function to create Linear Regression plots for "acousticness" and "loudness"
- fit the linear regression model
9. Compared Loudness vs. Danceability globally
- Calculate correlation coeeficient using Pearson's R correlation method
10. Compared Loudness vs. Danceability globally
- Calculate correlation coeeficient using Pearson's R correlation method
11. Compared Energy vs. Danceability globally
- Calculate correlation coeeficient using Pearson's R correlation method
12. Compared Speechiness vs. Valence globally
- Calculate correlation coeeficient using Pearson's R correlation method
13. Completed Regional Analysis
- Grouped data by countries by continent. We were hoping to learn whether different regions in the world had preferences by way of key features like: danceability, loudness, speechiness, valence, and duration
- Iterate through to create a dataframe by region for audio features - eastern_european, western_european, northern_european, african, east_asian, southeast_asian, south_asian, middle_eastern, latin_american, english_speaking 
- Visualized the world regional averages for each of the audio feature respectively
14. Displayed Top 50 playlist by country (Referred to I am sumat code)
- Def search_playlist(result, query) to return the playlist id from the result of the search method 
- Make sure the name of the playlist is the same one that we searched for and that it is made by Spotify (and not a user). Make both sides lowercase to make the comparison case-insenstive
- Used the Try Except block. While some countries do not return a playlist, it appears one or two return a playlist but that has no data in it, so we have to catch the IndexError this situation causes
- Had to hard code the list of countries that was outputted as a result of the prior cell because a lot of countries had extraneous words in them e.g. "republic of ..." 
- Pulled the 'Top 50 - <country name>' playlists for the countries in the list then create a dataframe and corresponding CSV for the playlist for each country
- Searched Spotify for the playlist (e.g. Top 50 - United States)
- Passed the search results to the search_playlist function to get back a playlist ID which is required to get the list of tracks in the playlist
- Only continued if the playlist ID search returned data
- Created list of tracks from the playlist to save into a CSV
- Got the track ids from the playlist and put them in a list. Used the ids to search songs and their features/analysis and then put that data in csv files by country
- Exported dataframe to csv before the first for loop moves to next country
15. Find values of the maximum and minumum values for each audio feature as well as the corresponding countries, then output the results into a table. 
-  First created a dictionary of audio features category, Max Country, Max Number and Min Country, Min Number. Find the max value for that column, index with the max value for that column. Here, the index is the country name. Find the min value for that column.Find the index with the min value for that column. Here, the index is the country name.  Converted dictionary created above into a dataframe
16. Plot the graph of each country vs each column (i.e. audio feature)
17. Visualize Taylor Swift top songs popularity by country
18. Completed audio feature analysis of Taylor Swift "Cruel Summer" popuarity =98
# Further Goals
1. Future statistical analysis suggested on whether specific music attributes influence a song’s popularity
2. With additional contextual data (popularity, user demographics / psychographics) could use to determine if music and songs should be tailored to country music attribute preference
3. Statistical comparison of individual country music attributes could use to determine if music and songs should be tailored to country specific music attributes
