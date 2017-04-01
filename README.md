# PyTwichBot

Welcome to PyTwitchBot decsription & documentation page.
PyTwitchBot is a twitch.tv chat bot written in Python 2.7. It contains several very interesting functions that allow you to interact with your viewers in a unique way. Below you can see documentation for each method and simple instructions how to set up PyTwitchBot.

The documentation is in progress of updating. I have added a lot of features and it became hard to keep track of all of them.
For now, version 3.2 is the latest one and I keep making changes to it. Thank you for using PyTwitchBot!

## Coins feature
PyTwBot now allows to use coins. Each command costs some amount of coins, and some commands gives viewers coins. For example,
request command gives user 50 starter coins.

## Set-up
### Running .exe
The only thing you need to do is to run PyTwitchBot.exe file and specify channel's name when program asks for it, or
### Running .py
You can call PyTwitchBot.py file from your command prompt:

```
python PyTwitchBot.py [channel's name]
```

### VK music streaming
PyTwitchBot will stream the music from the webpage into the file in /music_out.txt
Bot will prompt you for a link to the page with music.

## Functions and usage
All of the following commands should be typed in the channel's **chat**
### !help
Simply outputs all available commands with their cost

```
@Last updated: v. 3.1
> drazzzer: !help
> PyTwitchBot: !daily - 0 coins, !music - 0 coins, !next - 10 coins, !time - 0 coins, !vote [number] - 10 coins, !ask [question] - 25 coins, !followers - 0 coins, !uptime - 0 coins, !status - 0 coins, !request - 0 coins, !balance - 0 coins, !giveaway - 0 coins, !convert [link] - 100 coins, @drazzzer
```

### !daily
Gives a registered user (see @!status) 50 daily coins. 
Shows random gif from the folder /gifs/welcome/ and /gifs/source.gif will cointain either empty gif or the welcome gif.
/out/daily.txt will contain plain text with user's name and welcome message.

```
@Last updated: v. 3.2
> drazzzer: !daily
> PyTwitchBot: Hello, @drazzzer ! You have recieved your 50 daily coins!
```
![Image](https://pp.userapi.com/c604622/v604622947/4bbe2/Cb1ur24JkUI.jpg)


### !time
Show current time on the streamer's computer

```
@Last updated: v. 3.2
> drazzzer: !time
> PyTwitchBot: Current time: 02:18:10, @drazzzer
```

### !vote [parameters]
Has different cases:
#### Called by moderator
Starts a new poll with values specified.
Also, creates a new poll picture in the directory /out/VKPolls.png that is dynamically updated.

```
@Last updated: v. 3.2
> drazzzer: !vote one, two, three
> PyTwitchBot: Vote started: one, two, three, by @drazzzer
```

If poll existed before the call, stops it and returns the result

```
@Last updated: v. 2.0
> drazzzer: !vote one, two, three
> PyTwitchBot: Vote ended. Results: 1: 55%, 2: 45%, 3: 0%, @drazzzer
```

Example of the picture output:

![Image](https://pp.vk.me/c636421/v636421947/40ecf/X0K8JeRg7xo.jpg)

#### Called by a viewer

```
@Last updated: v. 2.0
> drazzzer: !vote 1
> PyTwitchBot: User: @drazzzer voted for 1
```

If there is no vote ongoing

```
@Last updated: v. 2.0
> drazzzer: !vote 1
> PyTwitchBot: There is no vote going right now, @drazzzer
```

### !ask [string]
Creates a file with a text of the question (UTF-8 ENCODING) in the directory out/question.txt. Also, plays a sound called alarm.mp3 in the current working directory.

```
@Last updated: v. 3.0
> drazzzer: !ask How are you doing?
> PyTwitchBot: New question asked by @drazzzer
```

Sample **question.txt** content:

```
Last question:
How are you doing? 
@drazzzer
```

### !followers
Shows the current number of followers.

```
@Last updated: v. 3.2
> drazzzer: !followers
> PyTwitchBot: Current number of followers: 28, @drazzzer
```

### !uptime
Shows the time of PyTwitchBot's uptime on the stream

```
@Last updated: v. 3.0
> drazzzer: !uptime
> PyTwitchBot: Current PyTwitchBot's uptime: 1 minutes, @drazzzer
```

### !status
Shows current status in the PyTwitchBot's database
See @!request

```
@Last updated: v. 1.0
> drazzzer: !status
> PyTwitchBot: You are moderator, @drazzzer
```

### !request
Processes a request from the caller to add him to the database. Allows him to use commands.
Also gives 50 starter coins.

```
@Last updated: v. 3.2
> drazzzer: !request
> PyTwitchBot: You can now use commands with 5 seconds cooldown, @drazzzer !
```

If user already in a database:

```
@Last updated: v. 3.2
> drazzzer: !request
> PyTwitchBot: You are already in a database, @drazzzer
```

### !balance
Shows user's balance in coins

```
@Last updated: v. 3.2
> drazzzer: !balance
> PyTwitchBot: Your balance is 922312 coins, @drazzzer
```

### !giveaway [#users] [#coins]
Starts a giveaway for #users and prize is #coins.

Moderator starts givaway:
```
@Last updated: v. 3.2
> drazzzer: !giveaway
> PyTwitchBot: Giveaway started by @drazzzer ! 100 coins can be won!
```

User participates:
```
@Last updated: v. 3.2
> someone: !giveaway
> PyTwitchBot: @someone is participating in a giveaway! Progress: ##### 50%
```
#users is reached:
```
@Last updated: v. 3.2
> someone: !giveaway
> PyTwitchBot: Giveaway winner is @someone! Won 100 coins.
```

#TODO: SQL DATABASE, SET COMMANDS DELAY, NEW FOLLOWER, PROFILE FILE
