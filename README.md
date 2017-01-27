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
![Image](https://pp.vk.me/c636421/v636421947/40ecf/X0K8JeRg7xo.jpg)
#### Called by a viewer
```
@Last updated: v. 1.0
> drazzzer: !vote one, two, three
> PyTwitchBot: Vote ended. Results: 1: 55%, 2: 45%, 3: 0%, @drazzzer
```

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/dkubatko/PyTwitchBot/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
