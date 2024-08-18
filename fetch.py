from printing import printLine
from colors import color
import requests
import json 

endColorLine = '\033[0m'

def fetchSong(song, printSpeed, artist = None):

    # Replace spaces in song name with underscores to fetch 
    song = '_'.join(str(x) for x in song) 
    
    request = None;
    if artist is not None: 
        artist = '_'.join(str(x) for x in artist) # Ditto
        request = requests.get(f'https://lyrist.vercel.app/api/{song}/{artist}')
    else: 
        request = requests.get(f'https://lyrist.vercel.app/api/{song}')
    
    response = json.loads(request.text)
    
    printLine(f"Playing {color['green']}{response['title']}{endColorLine} by {color['bold']}{response['artist']}{endColorLine}\n", pause=1000, speed=printSpeed)
    printLine(response["lyrics"], speed=printSpeed)
