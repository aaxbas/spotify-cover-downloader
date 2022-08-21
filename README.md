# spotify-cover-downloader
Spotify Cover Downloader can be used to download song album covers. It can also download a bunch of covers at once from a playlist!

## Requirements
- python3
- venv (or similar, optional)
- python-dotenv
- spotipy
- tqdm

## Initial Set-Up
Before using the program you must create a new app from the [Spotify for Developers Webpage](https://developer.spotify.com/dashboard/login) and get a `client_id` and `client_secret`. The access tokens can be put into a `.env` file (recommended) instead of hardcoding into the program, or passed as an argument to the program. 

### Example .env file
```sh
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

It is also recommended to use a virtual environment to run the program:

```sh
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Usage
```sh
python3 main.py https://open.spotify.com/playlist/3DIjw8eboATMgRN2RC6mz6 --directory Covers
```

Any spotify track (song), album or playlist URL,URI or ID will work!

### Additional Parameters
The following additional parameters can also be provided:
- `client_id`: your client_id (doesn't need to be passed if loaded as environment variable or in .env file)
- `client_secret`: your client_secret (doesn't need to be passed if loaded as environment variable or in .env file)
- `directory`: the directory to download the covers to. Defaults to "Covers/" if nothing passed.