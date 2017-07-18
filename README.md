# StalkerBot
Blip Blop this is the reddit stalker bot!

This is my very first Python script. Created to get a feel for the language.<br> 
The script uses [PRAW](https://praw.readthedocs.io/en/latest/) and [BeautifulSoup.](https://www.crummy.com/software/BeautifulSoup/)

This script will look for comments by the users you define and either insult or compliment them with a random message - depending on your mood I guess.
<br><br>

### Using the script
These installation steps are done in Arch Linux, for other distros the steps may vary.
<br><br>

**Download and configure the few variables in the script:**<br>
```python
# Users to stalk (comma separated array)
stalk = ['user1', 'user2', 'user3']

# True will insult the stalked individuals,
# False and it will compliment the users instead.
insult = True

# Define your Bot
client_id = ''
client_secret = ''
username = ''  # The reddit username for your Bot
password = ''  # The reddit password for your Bot
```
##### Tip: 
To create a Bot for Reddit, go to the preferences page of your Bot and select Apps. <br>
From here you can create a new Bot which will provide you with the `client_id` and `client_secret` values.
<br><br>

**Install the necessary packages:**<br>
`pacman -S python3 python-beautifulsoup4 python-praw`
<br><br>

**And run the script from your terminal:**<br>
`python3 stalker.py`
<br><br>

To cancel the script, use `Ctrl+C`
<br><br>

The insults are being fetched from: http://autoinsult.datahamster.com/ <br>
and the compliments are being fetched from: http://www.complimentgenerator.co.uk/
