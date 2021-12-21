import lyricsgenius
from colorama import Fore, init
from subprocess import check_output

# Raw Output from command
rawoutput = check_output(["rhythmbox-client", "--no-start", "--print-playing"], universal_newlines=True)

# Modify output to remove ".mp3" extension
output = rawoutput.replace('.mp3', '')

# Find artist name and song name
artistname = output.split('-', 1)[0]
songname = output.split('-', 1)[1]

# Print to show
print(artistname)
print(songname)

genius = lyricsgenius.Genius('XvnQ00lrQgH4Vs8G60WgtoGjMTCxdRWnZSMYR6_GI4ZluFmkhYGdnmjuq05U6bro')

# vv used for testing vv
# artistname = input("Artist Name: ")
# songname = input("Song Name: ")

# Search for song lyrics
artist = genius.search_artist(artistname, max_songs=3, sort="title")
song = artist.song(songname)

# Print song lyrics
print(song.lyrics)
print(f"\n{Fore.CYAN}Thank you for using {Fore.YELLOW}lyrics-displayer!{Fore.CYAN} This was made by me {Fore.YELLOW}*{Fore.GREEN}crue-ton{Fore.YELLOW}*{Fore.CYAN} on github!\n")