## HOW TO USE ##
- Set up a API Client on genius ([Click this to see how](https://github.com/crue-ton/rhythmbox-lyricfinder#how-to-set-up-genius-api-client))
- Just have a song playing on Rhythmbox
- Run the python file (Preferably just run the .sh file)
- Wait for it to to finish, and tada!
- You can also create an alias in your .bashrc, example:
```
alias lyric-finder="bash /home/geck/Py/rhythmbox-lyricfinder/run.sh"
```

## ACCESS KEY SET UP ##
- Go to https://genius.com/api-clients
- Make sure you've already set up a API client for this
- Select the API client you've created
- Click `Generate Access Token` which is under Client Access Token
- Go in to main.py
- Go to Line 19, and it should say `genius = lyricsgenius.Genius('Insert-Key-Here!')`
- Replace the text that is in the quotes with you Access Token

## MODULES TO INSTALL ##
Easiest method to do this is to run `pip install -r requirements.txt`
<p>But if you want to install these modules manually:</p>

- lyricsgenius
- colorama

## HOW TO SET UP GENIUS API CLIENT ##
- Go to https://https://genius.com/signup_or_login
- Create an account
- When your logged in, you should be redirected to https://genius.com/api-clients
- Click `New API Client`
- For the app name just put something like "Lyric Displayer" for easy identification
- Dont worry about the app icon, it is not needed
- For both the `App Wesbite URL` and `Redirect URL`, just put http://example.com/ in both fields
- Then Tada! You're Finished with the setting up the API Client!

## CREDITS ##
[crue-ton on github](https://github.com/crue-ton)
