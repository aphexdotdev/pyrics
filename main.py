from fetch import fetchSong
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("song", nargs='+', help='The name of the song')
parser.add_argument('--speed', type=int, help='Speed in milliseconds with which the lyrics should be printed')
parser.add_argument("--artist", nargs='+', help='The name of the artist. Optional but useful to better identify a song if only the name fails')

args = parser.parse_args()
if args.speed is None: args.speed = 50

if args.song:
    fetchSong(song=args.song, printSpeed=args.speed)

if args.artist:
    fetchSong(song=args.song, artist=args.artist, printSpeed=args.speed)