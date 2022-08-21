import os

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from tqdm import tqdm

from utils import download_image_url



class SpotifyCoverDownloader:

    def __init__(self,client_id=None, client_secret=None):

        if client_id and client_secret:
            self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        else:
            load_dotenv()
            self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))


    def download(self, url, directory):
        type = self.parse_url(url)
        if type == "track":
            self.download_song_cover(self.get_song(url), directory)
            return True
        elif type == "album":
            self.download_album_cover(self.get_album(url), directory)
            return True
        elif type == "playlist":
            self.download_covers(url, directory)
            return True
        return False


    def download_song_cover(self, song, directory, use_album_name=False):
        song_url = song['album']['images'][0]['url']
        
        if use_album_name:
            name = song['album']['name']
        else:
            name = song['name']

        if not os.path.exists(directory):
            os.makedirs(directory)

        download_image_url(song_url, os.path.join(directory, name.replace(':','_')))
    
    def download_album_cover(self, album, directory):
        album_url = album['images'][0]['url']
        name = album['name']

        if not os.path.exists(directory):
            os.makedirs(directory)

        download_image_url(album_url, os.path.join(directory, name.replace(':','_')))


    def get_song(self,url):
        return self.spotify.track(url)
    
    def get_album(self, url):
        return self.spotify.album(url)

    def download_covers(self, url, directory):
        results = self.spotify.playlist_tracks(url)
        songs = results["items"]
        
        while results['next']:
            results = self.spotify.next(results)
            songs.extend(results['items'])
        
        progress_bar = tqdm(songs)
        for song in progress_bar:
            progress_bar.set_description(f"Downloading Cover: {song['track']['name']}" )
            self.download_song_cover(song["track"], directory)


    def parse_url(self, url):
        if "playlist" in url:
            return "playlist"
        elif "album" in url:
            return "album"
        elif "track" in url:
            return "track"