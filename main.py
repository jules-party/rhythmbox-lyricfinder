import re
import lyricsgenius
from colorama import Fore, init
from subprocess import check_output

try:

	# Raw Output from command
	rawoutput = check_output(["rhythmbox-client", "--no-start", "--print-playing"], universal_newlines=True)

	# Modify output to remove ".mp3" extension
	output = rawoutput.replace('.mp3', '')

	# Find artist name and song name
	artistname = output.split('-', 1)[0]
	rawsongname = output.split('-', 1)[1]

	# Get rid of space before the rawsongname output
	songname = rawsongname[1:len(rawsongname)]
	# Print both artist name and the fixed song name
	print(artistname)
	print(songname)
	genius = lyricsgenius.Genius('T3xqBrhm_vB_829x_YNn63DbTLOUVlr5g_E6vQhD2nwk0FjxBCPSem7Bi0YqY1ZS')

	# vv used for testing vv
	# artistname = input("Artist Name: ")
	# songname = input("Song Name: ")

	# Search for song lyrics
	artist = genius.search_artist(artistname, max_songs=3, sort="title")
	song = artist.song(songname)

	# Removes those annoying hyperlinks at the end of the song lyrics, thank you ->
	# bdubs1991 and Vuizur on issue #218 on the lyricsgenius github repo!
	fixed_lyrics = re.sub(r"[0-9]+EmbedShare URLCopyEmbedCopy",'',song.lyrics)

	# Print song lyrics
	print(fixed_lyrics)
	print(f"\n{Fore.CYAN}Thank you for using {Fore.YELLOW}lyrics-displayer!{Fore.CYAN} This was made by me {Fore.YELLOW}*{Fore.GREEN}crue-ton{Fore.YELLOW}*{Fore.CYAN} on github!\n")

except IndexError:
	print('No Song Playing!')
