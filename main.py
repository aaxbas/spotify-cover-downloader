import argparse

from spotipy.oauth2 import SpotifyClientCredentials
from SpotifyCoverDownloader import SpotifyCoverDownloader


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Download Album Covers from Spotify")
    
    parser.add_argument("url", help="Song, album or playlist URLs")
    parser.add_argument("--directory", help="Directory to download covers", nargs="?",  default="Covers", const="Covers")
    parser.add_argument("--client_id", help="The Spotify Web App Client ID")
    parser.add_argument("--client_secret", help="The Spotify Web App Client Secret")

    args = parser.parse_args()
    
    spotify = SpotifyCoverDownloader(args.client_id,args.client_secret)
    spotify.download(args.url, args.directory)
