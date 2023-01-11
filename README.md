# Discord-Lobby-Status

on_voice_state_update: going to have the bot just listen to this, and any updates just re-write lol

might have this write to local flat file, and then another app just read it, idk LOL 
maybe a SNS topic lol

- pivoted to bot.run(), so basically this will decorate the bot with event listeners, then run it and constantly update SOMETHING(TBD) with list of strings, which some other program will listen to

-first step is to set up Discord.py to pull lobby status as app-bot from just my discord
(i should show the status of whos in lobby, PLUS like who was added or left in the last minute)


-Script to run this and display to screen all the members in a lobby 


-then have it default to displaying random important lobbies that i list 


-then have it be almost like a shell CLI almost, where i can spin up a service, identify good lobbies (add and remove), and close the service
