# rhythmbox-lyricfinder

![preview](https://github.com/crue-ton/rhythmbox-lyricfinder/blob/main/assets/preview.png?raw=true)

## HOW TO USE ##
- Just have a song playing on Rhythmbox
- Run:
```bash
rhythmbox-lyrcfinder
```
- Wait for it to to finish, and tada!

## HOW TO SET UP ##
- Clone this repo and then go into it
```bash
git clone https://github.com/crue-ton/rhythmbox-lyricfinder
cd rhythmbox-lyricfinder
```
- Refer to to ([This](https://github.com/crue-ton/rhythmbox-lyricfinder#how-to-set-up-genius-api-client)) and ([this also](https://github.com/crue-ton/rhythmbox-lyricfinder#access-key-setup)) to get everything setup.
- Run this when your done setting it up:
```bash
sudo make
or
doas make
```
- Then your done!

## HOW TO SET UP GENIUS API CLIENT ##
- Go to https://https://genius.com/signup_or_login
- Create an account
- When your logged in, you should be redirected to https://genius.com/api-clients
- Click `New API Client`
- For the app name just put something like "Lyric Displayer" for easy identification
- Dont worry about the app icon, it is not needed
- For both the `App Wesbite URL` and `Redirect URL`, just put http://example.com/ in both fields
- Then Tada! You're Finished with the setting up the API Client!

## ACCESS KEY SETUP ##
- Go to https://genius.com/api-clients
- Make sure you've already set up a API client for this
- Select the API client you've created
- Click `Generate Access Token` which is under Client Access Token
- Go in to main.py
- Go to line where it says: `genius = lyricsgenius.Genius('Insert-Key-Here!')`
- Replace the text that is in the quotes with your Access Token

## CREDITS ##
[crue-ton on github](https://github.com/crue-ton)
