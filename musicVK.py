from VKapi import connectVK as vkset
import warnings
import vk
import time 
warnings.filterwarnings("ignore")

DELAY = 5

def musicToFile(name = "music_out.txt", audio = {"artist": "None", "title": "None"}):
	'''Write contents to file'''
	f = open(name, "w")
	f.write(audio["artist"] + " - " + audio["title"])
	f.close()


def music_vk(link = "None", vk = None):
	#print("Connecting to VK")
	if (vk == None):
		vk = vkset(scope = "status")
	#print("Done")

	if (link == "None"):
		link = raw_input("User link: ")
	
	while (True):
		update_music(vk, link)
		time.sleep(DELAY)
	
def update_music(vk, link):
	try:
		user_id = vk.users.get(user_ids = link)[0]["uid"]
		response = vk.status.get(user_id=user_id)
		if ("audio" in response.keys()):
			audio = {}
			audio["artist"] = response["audio"]["artist"].encode("utf-8")
			audio["title"] = response["audio"]["title"].encode("utf-8")
			musicToFile(audio = audio)
		else:
			musicToFile()

	except vk.exceptions.VkAPIError:
		print "API exception!"
	
	

if (__name__ == "__main__"):
	music_vk()

