# PyTwichBot

Welcome to PyTwitchBot decsription & documentation page.
PyTwitchBot is a twitch.tv chat bot written in Python 2.7. It contains several very interesting functions that allow you to interact with your viewers in a unique way. Below you can see documentation for each method and simple instructions how to set up PyTwitchBot.

## Set-up
### Running .exe
The only thing you need to do is to run PyTwitchBot.exe file and specify channel's name when program asks for it, or
### Running .py
You can call PyTwitchBot.py file from your command prompt:

```
python PyTwitchBot.py [channel's name]
```

### Winamp
Unless you don't want to include music on your stream, you need to download winamp. Any version till v. 5.666 is supported.

## Functions and usage
All of the following commands should be typed in the channel's **chat**
### !help
Simply outputs all available commands

```
@Last updated: v. 1.0
> drazzzer: !help
> PyTwitchBot: !hi, !music, !next, !time, !vote, !question, !followers, !status, @drazzzer
```

### !hi
Bot responds to the hi message from the viewer

```
@Last updated: v. 1.0
> drazzzer: !hi
> PyTwitchBot: Hello, @drazzzer!
```

### !music
Shows name of the current track playing in **Winamp**

```
@Last updated: v. 1.0
> drazzzer: !music
> PyTwitchBot: Now playing: Blackmill - My Love, @drazzzer
```

### !next
Processes one vote for changing the music to the next track in **Winamp**
(See @!setnextt)

```
@Last updated: v. 1.0
> drazzzer: !next
> PyTwitchBot: Votes to change music: 1
```

If number of votes >= threshhold:

```
@Last updated: v. 1.0
> drazzzer: !next
> PyTwitchBot: Changing song...
```

### !time
Show current time on the streamer's computer

```
@Last updated: v. 1.0
> drazzzer: !time
> PyTwitchBot: Current time: 02:18:10, @drazzzer
```

### !vote [parameters]
Has different cases:
#### Called by moderator
Starts a new poll with values specified.
Also, creates a new poll picture in the directory /out/VKPolls.png that is dynamically updated.

```
@Last updated: v. 1.0
> drazzzer: !vote one, two, three
> PyTwitchBot: Vote started: one, two, three, by @drazzzer
```

If poll existed before the call, stops it and returns the result

```
@Last updated: v. 1.0
> drazzzer: !vote one, two, three
> PyTwitchBot: Vote ended. Results: 1: 55%, 2: 45%, 3: 0%, @drazzzer
```

Example of the picture output:

![Image](https://pp.vk.me/c636421/v636421947/40ecf/X0K8JeRg7xo.jpg)

#### Called by a viewer

```
@Last updated: v. 1.0
> drazzzer: !vote 1
> PyTwitchBot: User: @drazzzer voted for 1
```

If there is no vote ongoing

```
@Last updated: v. 1.0
> drazzzer: !vote 1
> PyTwitchBot: There is no vote going right now, @drazzzer
```

### !ask [string]
Creates a file with a text of the question (UTF-8 ENCODING) in the directory out/question.txt. Also, plays a sound called alarm.mp3 in the current working directory.

```
@Last updated: v. 1.1
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
@Last updated: v. 1.0
> drazzzer: !followers
> PyTwitchBot: Current number of followers: 28, @drazzzer
```

### !uptime
Shows the time of PyTwitchBot's uptime on the stream

```
@Last updated: v. 1.0
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

```
@Last updated: v. 1.0
> drazzzer: !request
> PyTwitchBot: You can now use commands with 5 seconds cooldown, @drazzzer !
```

If user already in a database:

```
@Last updated: v. 1.0
> drazzzer: !request
> PyTwitchBot: You are already in a database, @drazzzer
```


#TODO: SQL DATABASE, MODERATOR ADD, SET COMMANDS DELAY, NEW FOLLOWER
