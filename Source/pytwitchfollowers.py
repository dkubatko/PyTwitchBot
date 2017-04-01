import requests, json, socket, time
import warnings
warnings.filterwarnings("ignore")

HOST = "irc.twitch.tv"
NICK = "drazzzer"
PORT = 6667
PASS = "oauth:ahgunrf9si6ks50aglgl2kjtoc7k9e"
readbuffer = ""
MODT = False
flag = True
s = socket.socket()


def turnOff():
   flag = False

def before():
   s.connect((HOST, PORT))
   s.send("PASS " + PASS + "\r\n")
   s.send("NICK " + NICK + "\r\n")
   s.send("JOIN #drazzzer \r\n")
   print "Connected to chat! #FollowsBot"

def Send_message(message):
    s.send("PRIVMSG #drazzzer :" + message.encode('utf-8') + "\r\n")
    
def main():
   headers = {'Accept': 'application/vnd.twitchtv.v2+json', "Client-ID":'atoljvzdzcdf951gbw60ey9lpghcgv'}
   r_get = requests.get("https://api.twitch.tv/kraken/channels/drazzzer/follows", headers = headers)
   data = r_get.json()
   old_count = data['_total']
   print 'Starting.... Press CTRL + C to Quit'

   while flag:
      r_get = requests.get("https://api.twitch.tv/kraken/channels/drazzzer/follows", headers = headers)
      data = r_get.json()
      if data['_total'] > old_count:
         print data['_total']
         username = data['follows'][0]['user']['display_name']
         try:
            line = "Огромное спасибо за подписку, ".decode('utf-8')
            Send_message(line + username + "!")
            old_count = data['_total']
         except:
            print 'You did not set up sockets properly!!!'
         
      try:
         for i in range(5):
            time.sleep(0.1)
      except:
         break
      
import twitch.api.v3 as tw

def get_data():
   data = tw.channels.by_name("drazzzer")
   print data["followers"]
   #for follower in data:
   #   print follower['channel']['name']

if __name__ == '__main__':
   before()
   main()
