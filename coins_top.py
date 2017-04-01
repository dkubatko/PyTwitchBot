import operator

def top_coins(coins, file, mods):
	f = open(file, 'w')
	new = {}
	for elem in coins:
		if elem not in mods:
			new[elem] = coins[elem]
			
	top3 = sorted(new.items(), key=operator.itemgetter(1), reverse = True)[:3]
	f.write("Top viewers:\n")
	for elem in top3:
		f.write(str(elem[0]) + ' - ' + str(elem[1]) + " coins\n")
	f.close()
