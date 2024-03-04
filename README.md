
# SourceTwitchIntergration

A Python script meant to make it so a twitch streamer can have their chat interact with the game through RCON.

## Setup

- Plugins: Please install all plugins in requirements.text to your envirnment.

- Twitch Information
  - Access Token: Go to : https://twitchtokengenerator.com/ and follow their instructions on how to generate your access token. There are alternative methods if you would like to use a more secure method. **Never give this to anyone!**

- Config File: Run Bot.py once to generate config.cfg
  - Under [Twitch Information] replace USERNAME in the quotation marks with your username in lowercase. It should look something like this, ```username = "burchburch"```.
  - Replace TOKEN with your access token in the same way as your username. ```access_token = "wadawdfoiesfuiehfisuohefpp309j"```. Don't use this. It is not a real token.

- Launch Options: There should be a file called rcon.cfg copy the section of the file that it tells you to into source games launch options.
- Then put rcon.cfg into `Team Fortress 2/tf/cfg`

## Running It

Now that you have finished configuration you can get to the real fun. Pure chaos with your chat faffing about with your controls and all sorts of things.

## This is still under contruction

Many things are still incomplete, this document is a good example of that. Please be pateint with me while I work out the kinks.

Missing feature:

- Async on commands
- Easy custom commands
