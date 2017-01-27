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
### !question [string]
### !followers
### !status
