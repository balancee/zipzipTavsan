# zipzipTavsan
This project consists of a single python script which exploits the lack of control on the http requests sent to a game called zipzipTavsan, to have eventually enabled the user to submit the desired "username" and "score"
to the leaderboard of the game as opposed to actually playing the game in a flash container.

second line defines a reference to the url of the exploited game.
payload variable holds the content of the data which are to be posted to the required php application
**IMPORTANT**
'gameid':'145' should not change. Since its the ID of the zipzipTavsan game.
