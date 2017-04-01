import socket, string, requests, json
import winamp_api as w
import datetime
import time
import musicVK
from playsound import playsound
import pic_generator as pg
from speech import speech
import warnings
import sys
import os
import pyttsx
from shutil import copyfile
import threading
import glob
import random
import vk
import image_conversion


warnings.filterwarnings("ignore")

VERSION = "3.1"
AUTHOR = "drazzzer"

print("Verson: v" + VERSION + "\nAuthor: " + AUTHOR) 

print ("Connecting to VK api...")
failed_vk = False
try:
    session = vk.AuthSession(app_id = '5813182', user_login = '89296301367',
                             user_password = 'danjusha', scope = "status, wall")
    api = vk.API(session)
    print "Successful"
except:
    print "Failed"
    failed_vk = True






link = raw_input("Music link: ")
t = threading.Thread(target = musicVK.music_vk, args = (link, api))
t.daemon = True
t.start()







#method to initialize moderators
def init_mods(filename):
    try:
        f = open(filename)
        f.close()
    except:
        "You don't have a database called " + filename
        return []
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

def write_to_file_d(filename, dic):
    try:    
        f = open(filename, 'w')
        for item in dic:
            f.write(item + ' ' + str(dic[item]) + '\n')
        f.close()
    except:
        Send_message("You don't have a database called " + filename)
        return

def write_to_file(filename, data):
    try:
        f = open(filename, 'w')
        for item in data:
            f.write(item + '\n')
        f.close()
    except:
        Send_message("You don't have a database called " + filename)
        return


moderators = []

#Get arguments from command line
try:
    owner = str(argv[1])
    moderators.append(str(argv[1]))
except:
    owner = raw_input("Channel owner: ")
    moderators.append(owner)

filename_m = "moderators_" + owner + '.pyt'


###############################
#####VK post processing########
if (not failed_vk):
    grouplink = ''

    try:
        grouplink = str(argv[2])
    except:
        grouplink = raw_input("VK group link: ").split('/')[-1]


    if (grouplink != ''): 
        id = api.groups.getById(group_id=grouplink)[0]["gid"]
        print id
        api.wall.post(owner_id = "-" + str(id), message = "Stream is online! twitch.tv/" + owner, attachments="photo158563947_456239331")


##############################

moderators.extend(init_mods(filename_m))

s = socket.socket()

################
old_count = 0
filename_f = "followers_" + owner + '.pyt'

copyfile(filename_f, "backup/" + filename_f)
copyfile(filename_m, "backup/" + filename_m)


followers = []
coins = {}
daily_got = {}
daily_got[owner] = False
followers.extend(init_mods(filename_f))
for i in range(len(followers)):
	data = followers[i].split(" ")
	followers[i] = data[0]
	coins[data[0]] = int(data[1])
	daily_got[data[0]] = False

start_coins = 50
daily_coins = 50

################
threshold = 5
delay = 0
time_elapsed = 0
start_time = 0
uptime = 0
flag = True
#votes count for songs
songs = 0
songs_voters = []

command_cooldowns = {}
cooldown = 5

vote_options = []
vote_results = []
voted_users = []


submode = False
followmode = False
slowmode = False

# Method to say hi
def get_daily(user, args):
    global coins
    global daily_coins
    global daily_got
    if (not daily_got[user]):
        coins[user] += daily_coins
        Send_message("Hello, @" + user + "! You have recieved your " + str(daily_coins) + " daily coins!")
        daily_got[user] = not daily_got[user]
        update_top()

        lis = glob.glob("gifs/welcome/*.gif")
        rand = random.randint(0, len(lis) - 1)
        print rand

        copyfile(lis[rand], "gifs/source.gif")
        
        f = open("out/daily.txt", "w")
        s = user + " just recieved daily coins!"
        f.write(s)
        f.close()

        playsound("daily.mp3")

        time.sleep(5)

        f = open("out/daily.txt", "w")
        f.close()
        time.sleep(0.1)
        copyfile("gifs/empty.gif", "gifs/source.gif")
        
        
    else:
        Send_message("You have already used daily bonus, @" + user)

    
# Method to get track name
def getTrackName(user, args):
    win = w.winamp()
    track_name = win.getCurrentTrackName()
    track_name = track_name.split(' - ')[0][3:] + ' - ' + track_name.split(' - ')[1]
    track_name = track_name.decode('cp1251')
    
    Send_message("Now playing: ".decode('utf-8') + track_name + ", @" + user)


#method to show current time
def show_time(user, args):
    time = str(datetime.datetime.now().time()).split('.')[0]
    Send_message('Current time: ' + time + ', @' + user)

#method to start new vote by moderator or vote for user
def start_vote(user, arr):
    global vote_results
    global vote_options
    global vote_results
    global voted_users
    global moderators
    if user in moderators:
        if vote_options != []:
            out = "Results: "
            summ = sum(vote_results)
            if (summ == 0):
                summ = 1
            
            i = 1
            for elem in vote_results:
                out += str(i) + ": " + str(int(elem * 100 / summ)) + '%, '
                i += 1
                
            out += "@" + user
            Send_message('Vote ended. ' + out)
            vote_options = []
            vote_results = []
            voted_users = []
            return
        else:
            votes = arr.split(', ')
            out = ''
            for elem in votes:
                vote_options.append(elem)
                vote_results.append(0)
                out += elem.decode('utf-8') + ', '
            data = {}
            data['answers_count'] = len(vote_results)
            data['question'] = "Recent twitch.tv poll by @" + user
            data['answers'] = []
            for i in range(len(vote_options)):
                elem = vote_options[i]
                summ = sum(vote_results)
                if (summ == 0):
                    summ = 1
                rate = vote_results[i] * 100 / summ
                data['answers'].append({'text':elem.decode('utf-8'), 'rate': rate})
                    
            pg.new_img(data, 300, 70, (255, 255, 255), 25, (0, 0, 0, 100), 3)
                    
            Send_message('Vote started: ' + out + ' by @' + user)
    else:
        if vote_results != []:
            if user in voted_users:
                Send_message("You have already voted, @" + user)
            else:
                ind = int(arr)
                if ind <= len(vote_results):
                    vote_results[ind - 1] += 1
                    voted_users.append(user)
                    Send_message("User: @" + user + " voted for " + str(ind))

                    data = {}
                    data['answers_count'] = len(vote_results)
                    data['question'] = "Recent twitch.tv poll\n by @" + user
                    data['answers'] = []
                    for i in range(len(vote_options)):
                        elem = vote_options[i]
                        summ = sum(vote_results)
                        if (summ == 0):
                            summ = 1
        
                        rate = vote_results[i] * 100 / summ
                        data['answers'].append({'text':elem.decode('utf-8'), 'rate': rate})
                    
                    pg.new_img(data, 300, 70, (255, 255, 255), 25, (0, 0, 0, 100), 3)
                else:
                    Send_message("No such vote option, @" + user)
        else:
            Send_message("There is no vote on right now, @" + user)


######################################
#Giveaway data#
give_on = False
give_data = {'users': [], 'max_count': 0, 'sum': 0}
def giveaway(user, args):
    global give_on
    if user in moderators:
        start_giveaway(user, args)
    else:
        if (give_on):
            part_giveaway(user)
        else:
            Send_message("There is no giveaway going on, @" + user)


def start_giveaway(user, args):
    global give_data
    global give_on
    if (not give_on):
        count = args.split(' ')[0]
        summ = args.split(' ')[1]
        give_data["max_count"] = int(count)
        give_data["sum"] = int(summ)
        give_on = True

        f = open("out/giveaway.txt", "w")
        f.write("!giveaway is live for " + str(give_data["sum"]) + " coins!")
        f.close()

        Send_message("/me Giveaway started by @" + user + "! " + str(give_data["sum"]) + " coins can be won!")
    else:
        f = open("out/giveaway.txt", "w")
        f.close()
        Send_message("/me Giveaway stopped by @" + user)
        give_data = {'users': [], 'max_count': 0, 'sum': 0}
        give_on = False
        


def part_giveaway(user):
    global give_data
    global give_on
    global coins
    give_data["users"].append(user)
    if (len(give_data["users"]) >= give_data["max_count"]):
        winner = get_winner(give_data)
        coins[winner] += give_data["sum"]
        f = open("out/giveaway.txt", "w")
        f.close()
        Send_message("/me Giveaway winner is @" + winner + "! Won " + str(give_data["sum"]) + " coins.")
    else:
        Send_message("/me @" + produce_out(user, give_data))


def get_winner(data):
    r = random.randint(0, data["max_count"] - 1)
    return data["users"][r]

def produce_out(name, data):
    cur = len(data["users"])
    maxc = data["max_count"]
    ratio = int((cur / float(maxc)) * 10)
    s = name + " is participating in a giveaway! Progress: " + "#"*ratio + " " + str(int(cur / float(maxc) * 100)) + "%"
    return s 

################################
#end of giveaway part#

#ask question on a stream
def show_question(user, question):
    global start_time
    global delay
    global time_elapsed
    question_text = question
    time_elapsed = time.time() - start_time
    if time_elapsed >= delay:
        question = question.decode('utf-8')
        f = open("out/question.txt", 'w+')
        f.truncate()
        question = split_string(question)
        out = "Last question:\n" + question + '\n@'+ user
        f.write(out.encode("utf-8"))
        f.close()
        playsound("alarm.mp3")
        Send_message("New question asked by @" + user)
        engine = pyttsx.init()
        speech(question_text, engine)
        start_time = time.time()
    else:
        Send_message("Command !ask cooldown is " + str(int(delay - time_elapsed)) + " seconds, @" + user)
    
#show available followers
def show_help(user, args):
    global options_names
    global options_prices
    options = options_names
    out = ""
    for elem in options:
        out += elem + ' - ' + str(options_prices[elem[1:].split(' ')[0]]) + ' coins, '

    Send_message(out + "@" + user)

#shows balance for a user
def balance(user, args):
	global coins
	Send_message("Your balance is " + str(coins[user]) + " coins, @" + user)

def show_uptime(user, args):
    global uptime
    Send_message("Current PyTwitchBot's uptime: " + str(int(uptime / 3600.0)) + " hours " + str(int(uptime % 3600.0 / 60)) + 
         " minutes, @" + user)

def convert_image(user, args):
    link = str(args)
    result = image_conversion.convert_image(link)
    if (result != "Bad link"):
        Send_message(result)
        Send_message("Image converted for @" + user)
    else:
        Send_message("Bad link, @" + user)



#######################################
########Moderators commands############
#######################################

#show available followers
def show_help_mod(user, args):
    global options_mod
    global moderators
    if user in moderators:
        options = options_mod
        out = ""
        for elem in options:
            out += elem + ' - ' + str(options_prices[elem[1:].split(' ')[0]]) + ' coins, '

        Send_message(out + "@" + user)
    else:
        Send_message("Sorry, you don't have access to this command, @" + user)
        
#add user to the list of moderators
def add_mod(user, to_add):
    global moderators
    global filename_m
    if user in moderators:
        moderators.append(to_add.lower())
        write_to_file(filename_m, moderators)
        Send_message("Sucessfully added mod @" + to_add + " by @" + user)
    else:
        Send_message("Sorry, you don't have access to this command, @" + user)

#del user to the list of moderators
def del_mod(user, to_del):
    global moderators
    global owner
    global filename_m
    if user == owner:
        try:
            moderators.remove(to_del.lower())
            write_to_file(filename_m, moderators)
            Send_message("Sucessfully removed mod @" + to_del + " by @" + user)
        except:
            Send_message("No such user, @" + user)
    else:
        Send_message("Sorry, you don't have access to this command, @" + user)

#show number of followers
def show_followers(user, args):
    global old_count
    Send_message("Current number of followers: " + str(old_count) + ", @" + user)

#get status of the specified user
def show_status(user, args):
    global moderators
    global followers
    if user in moderators:
        Send_message("You are moderator, @" + user)
    elif user in followers:
        Send_message("You are allowed to use commands, @" + user)
    else:
        Send_message("Ooops, I don't see you in the database :( Try to follow my channel @" + user)

#set threshhold for changing music        
def set_treshhold(user, value):
    global moderators
    global threshold
    if (user in moderators):
        threshold = int(value)
        Send_message("Succesfully set !next threshold to " + str(threshold) + ", @" + user)
    else:
        Send_message("Sorry, you don't have access to this command, @" + user)

#method to change the song if count is more then threshld
def change_song(user, args):
    global songs
    global songs_voters
    global threshold
    
    if user not in songs_voters:    
        
        songs += 1
        if songs >= threshold:
            Send_message("Changing song...".decode('utf-8'))
            win = w.winamp()
            win.command('next')
            songs = 0
            songs_voters = []
        else:
            songs_voters.append(user)
            Send_message("Votes to change music: ".decode('utf-8') + str(songs))
    else:
        Send_message("You have already voted, @".decode('utf-8') + user)

#set command delay
def set_command_delay(user, value):
    global cooldown
    if (user in moderators):
        cooldown = int(value)
        Send_message("Succesfully set commands cooldown to " + str(cooldown) + ", @" + user)
    else:
        Send_message("Sorry, you don't have access to this command, @" + user)

#close program
def close(user, value):
    global owner
    global flag
    if (user == owner):
        Send_message("Bye, @" + user + "!")
        flag = False

#set ask delay
def set_delay(user, value):
    global moderators
    global delay
    if (user in moderators):
        delay = int(value)
        Send_message("Succesfully set !ask delay to " + str(delay) + ", @" + user)
    else:
        Send_message("Sorry, you don't have access to this command, @" + user)

#turn on or turn off submode
def set_submode(user, args):
    global moderators
    global submode
    if user in moderators:
        if (not submode):
            Send_message("/subscribers")
            submode = not submode
        else:
            Send_message("/subscribersoff")
            submode = not submode
    else:
        Send_message("This is moderators-only command, sorry @" + user)

#turn on or turn off followers mode
def set_followers(user, args):
    global moderators
    global followmode
    if user in moderators:
        if (not followmode):
            Send_message("/followers")
            followmode = not followmode
        else:
            Send_message("/followersoff")
            followmode = not followmode
    else:
        Send_message("This is moderators-only command, sorry @" + user)

#turn on or turn off slowmode
def set_slowmode(user, args):
    global moderators
    global slowmode
    if user in moderators:
        if (not slowmode):
            Send_message("/slow")
            slowmode = not slowmode
        else:
            Send_message("/slowoff")
            slowmode = not slowmode
    else:
        Send_message("This is moderators-only command, sorry @" + user)

#clean chat
def clear(user, args):
    global moderators
    if user in moderators:
        Send_message("/clear")
    else:
        Send_message("This is moderators-only command, sorry @" + user)


#give money to user
def give(user, args):
    global moderators
    if user in moderators:
        name = args.split(' ')[0]
        value = int(args.split(' ')[1])
        try:
            if coins[user] >= value:
                if (value > 0):
                    coins[name] += value
                    coins[user] -= value
                    update_top()
                    update_balance()
                    Send_message("Successfully transfered " + str(value) + " coins from @" + user + " to @" + name)
                else:
                    Send_message("You can't transfer negative sum, @" + user)
            else:
                Send_message("You don't have enough coins, @" + user + ", check !balance")
        except:
            Send_message("No such user, @" + user)
    else:
        wSend_message("This is moderators-only command, sorry @" + user)

####################################

#update followers list
def update_followers(user, args):
    global followers
    global cooldown
    global coins
    global filename_f
    global start_coins
    global daily_got
    if user not in followers:
        followers.append(user)
        daily_got[user] = False
        command_cooldowns[user] = 0
        coins[user] = start_coins
        write_to_file_d(filename_f, coins)
        Send_message("You can now use commands with	" + str(cooldown) + " seconds" +
                     " cooldown, @" + user + "! Also, you got " + str(start_coins) + " starter coins.")
    else:
        Send_message("You are already in a database, @" + user)

def update_balance():
	global filename_f
	global coins

	f = open(filename_f, "w")
	for elem in coins:
		f.write(elem + ' ' + str(coins[elem]) + '\n')
	f.close()

def update_top():
    global coins
    global moderators
    from coins_top import top_coins
    fname = "out/coinstop.txt"
    top_coins(coins, fname, moderators)

#split string so it fits on one line
def split_string(s):
    arr = s.split(' ')
    i = 0
    res = ''
    for elem in arr:
        if i >= 5:
            res += '\n'
            res += elem + ' '
            i = 1
        else:
            res += elem + ' '
            i+=1
    return res


# Method for sending a message
def Send_message(message):
    global owner
    s.send("PRIVMSG #" + owner + " :" + message.encode('utf-8') + "\r\n")

# Method for doing the commands
def Run_command(cmd, user, parameters):
    global coins
    global options_prices
    try:
        if (coins[user] >=  options_prices[cmd]):
            t = threading.Thread(target = Process_command, args = (cmd, user, parameters))
            t.daemon = True
            t.start()
            coins[user] -= options_prices[cmd]
            update_balance()
        else:
        	Send_message("You don't have enough coins for this command, @" + user + ", check !balance")
    except:
        options[cmd](user, parameters)

def Process_command(cmd, user, parameters):
    try:
        options[cmd](user, parameters)
    except:
        Send_message("Wrong usage of " + cmd + ", @" + user)

    

options = {'daily': get_daily, 'music': getTrackName, 'next':change_song, 'time':show_time,
           'help':show_help, 'followers':show_followers, 'status':show_status, 'submode':set_submode,
            'followmode':set_followers, 'clear':clear, 'slowmode':set_slowmode, 'request':update_followers,
           'helpmod':show_help_mod, 'uptime':show_uptime, 'addmod':add_mod, 'vote':start_vote, 'ask':show_question,
           'setnextt':set_treshhold, 'setdelay':set_delay, 'setcd':set_command_delay, 'give':give, 'balance':balance, 'delmod':del_mod, 'exit':close,
           'giveaway':giveaway}

options_names = ['!daily', '!music', '!next', '!time', '!vote [number]',
 '!ask [question]', '!followers', '!uptime', '!status', '!request', '!balance', '!giveaway', '!convert [link]']

options_mod = ['!slowmode', '!submode', '!followmode', '!setnextt [value]', '!setdelay [value]',
                '!vote [options]', '!addmod [username]', '!setcd [value]', '!give [name] [value]', '!giveaway [max users] [coins]']

options_prices = {'daily': 0, 'music': 0, 'next': 10, 'time': 0,
           'help': 0, 'followers': 0, 'status': 0, 'submode': 50,
            'followmode': 50, 'clear': 50, 'slowmode': 50, 'request': 0,
           'helpmod': 0, 'uptime': 0, 'addmod': 1000, 'vote': 10, 'ask': 25,
           'setnextt': 100, 'setdelay': 100, 'setcd': 100, 'give': 0, 'balance': 0, 'delmod': 0, 'exit': 0, 'giveaway': 0, 'convert':100}


def main():
    global owner
    # Set all the variables necessary to connect to Twitch IRC
    HOST = "irc.twitch.tv"
    NICK = "pytwbot"
    PORT = 6667
    PASS = "oauth:q6a7w8g5ctvqfjjy2oyhozhcu88h3a"
    readbuffer = ""
    MODT = False
    global old_count
    global followers
    global uptime
    global moderators
    global command_cooldowns
    global cooldown
    headers = {'Accept': 'application/vnd.twitchtv.v5+json', "Client-ID":'83lf083si5ulzwzz8jjs1aoxqrokyv'}
    r_get = requests.get("https://api.twitch.tv/kraken/users?login=" + owner, headers = headers)
    data = r_get.json()
    user_id = data['users'][0]['_id']
    r_get = requests.get("https://api.twitch.tv/kraken/channels/" + user_id + "/follows", headers = headers)
    data = r_get.json()
    old_count = data['_total']
    print 'Initial followers count: ' + str(old_count)
    # Connecting to Twitch IRC by passing credentials and joining a certain channel


    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    s.send("JOIN #" + owner + "\r\n")

    ##############################
    initial_time = time.time()
    old_time = time.time()
    ##############################

    print 'Connected to #' + owner + ' - PyTwitchBot'
    Send_message("PyTwitchBot connected!")
    Send_message("/color red")
    update_top()

    while flag:
        #####################################
        r_get = requests.get("https://api.twitch.tv/kraken/channels/" + user_id + "/follows", headers = headers)
        data = r_get.json()
        if data['_total'] > old_count:
         print data['_total'] 
         username = data['follows'][0]['user']['display_name']
         try:
            f = open("out/followers.txt", "w+")
            f.write("Last follower:\n" + username + "\nWelcome!")
            f.close()
            line = "Thanks for following, @".decode('utf-8')
            playsound("follower.mp3")
            Send_message(line + username + "!")
            old_count = data['_total']
         except:
            print 'You did not set up sockets properly!!!'
        #####################################
        
        try:
            readbuffer = readbuffer + s.recv(1024)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            s.close()
            break

        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        elapsed_time = time.time() - old_time
        uptime += elapsed_time
        for elem in command_cooldowns.keys():
            command_cooldowns[elem] -= elapsed_time
        old_time = time.time()
        
        
        for line in temp:
            # Checks whether the message is PING because its a method of Twitch to check if you're afk
            if ("PING" in line.split(' ')):
                s.send("PONG %s\r\n" % line[1])
            else:
                # Splits the given string so we can work with it better
                #print line
                parts = string.split(line, ":")
                
                if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                    try:
                        # Sets the message variable to the actual message sent
                        try: 
                            rest = ''.join(parts[3:])
                        except:
                            rest = ''
                        message = parts[2][:len(parts[2]) - 1] + rest
                    except:
                        message = ""
                    # Sets the username variable to the actual username
                    usernamesplit = string.split(parts[1], "!")
                    username = usernamesplit[0]
                    # Only works after twitch is done announcing stuff (MODT = Message of the day)
                    if MODT and message != '':
                        #print username + ": " + message.decode("utf-8")
                        if (message[0] == '!'):
                            command = message[1:].split(' ')
                            if ((username not in followers) and (username not in moderators)):
                                if (command[0] == 'help' or command[0] == 'status' or command[0] == 'request'):
                                    Run_command(command[0].lower(), username, ' '.join(command[1:]))
                                else:
                                    Send_message("Sorry, you can not use commands :( @" + username + " Try !request")               
                            else:
                                try:
                                    if (username not in command_cooldowns.keys()):
                                        command_cooldowns[username] = 0

                                    if (username in moderators) or (command_cooldowns[username] <= 0):
                                        Run_command(command[0].lower(), username, ' '.join(command[1:]))
                                        
                                        if username not in moderators:
                                            command_cooldowns[username] = cooldown
                                except:
                                    Send_message('No such command, @' + username + "!")

                    for l in parts:
                        if "End of /NAMES list" in l:
                            MODT = True

if __name__ == "__main__":
    main()

'''elif command[0] == 'vote':
                                try:
                                    start_vote(username, ' '.join(command[1:]))
                                except:
                                    Send_message('Wrong input for !vote (!vote [number]), @' + username) 
                            elif (command[0] == 'ask'):
                                show_question(username, ' '.join(command[1:]))
                            elif command[0] == 'setnextt':
                                try:
                                    set_treshhold(username, int(''.join(command[1:])))
                                except:
                                    Send_message('Wrong input for !setnextt (!setnextt [number]), @' + username)
                            elif command[0] == 'setdelay':
                                try:
                                    set_delay(username, int(''.join(command[1:])))
                                except:
                                    Send_message('Wrong input for !setdelay (!setdelay [number]), @' + username) '''
