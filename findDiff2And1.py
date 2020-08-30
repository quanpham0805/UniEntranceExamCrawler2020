mydict = {}
mylist = []

file = open("ListOfID1.txt", "r", encoding = "UTF-8")
contents1 = file.readlines()
file.close()

file = open("ListOfID2.txt", "r", encoding = "UTF-8")
contents2 = file.readlines()
file.close()

for i in contents1:
	mydict[i] = 0

for i in contents2:
	mydict[i] = 0

for i in contents1:
	mydict[i] += 1

for i in contents2:
	mydict[i] += 1

for i in mydict.keys():
	if mydict[i] == 2:
		continue
	mylist.append(i)

with open("ListOfIDDiff.txt", "w", encoding = 'UTF-8') as writeFile:
		for keys in mylist:
			writeFile.write(str(keys))

writeFile.close()