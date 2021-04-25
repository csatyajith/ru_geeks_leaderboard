# ru_geeks_leaderboard
A leaderboard for practice problems solved by RU 2021 CS Geeks group!

In case you want to run it locally, you need to do the following things:
1. Get a list of participants GitHub accounts.
2. Get an OAuth Token for a slack bot. This bot should also have chat:write permission set to True.
3. Create a file locally in the config folder with the name "local-config.json". The keys should be the same as
the "config-template.json". Change the values according to your preferences.
   
When you run the slack client, you will probably encounter a certificate error. 
I found this link useful to counter that: https://github.com/slackapi/python-slack-sdk/issues/334#issuecomment-433498349