#########################################################################################
# Instruction:
# Modify only the constant values as instructed
# run the code by navigating the cmd to the folder of this file, then type
# python dataProcessor.py
#########################################################################################


import ast
import sys

# What the program will do is generating all the following files in the written order.

# This file is the input file, the crawled data file, the raw file
CONST_DATA_FILE = "newtemp.txt"

# This file will contain the data after it was sorted
CONST_CLEANED_DATA = "CleanedData.txt"

# This file will contain the above data, but with duplicates removed
# i.e, the final file. You will use this file for the Visualization file
CONST_DATA_NO_DUP = "CleanedDataNoDup.txt"

# This file will contain the missing SBD,
# assuming the first and last SBD of a cumthi is correct.
CONST_MISSING_DATA = "MissingData.txt"


#########################################################################################
# Do not modify the code below unless you know exactly what you are doing
#########################################################################################

data = []

def getData(path):
	data.clear()
	file = open(path, "r", encoding = "UTF-8")
	contents = file.readlines()
	file.close()

	dem = 0
	for i in contents:
		try:
			zzz = ast.literal_eval(i)
		except:
			dem += 1
			continue
		data.append(zzz)

	print("Corrupted data from ", path, ": ", dem)


def CleanUp():
	getData(CONST_DATA_FILE)
	data.sort(key=lambda k: (k['cumthi'], k['SBD']))
	with open(CONST_CLEANED_DATA, "w", encoding = 'UTF-8') as writeFile:
		for i in range(len(data)):
			writeFile.write(str(data[i]))
			writeFile.write(str('\n'))

	writeFile.close()


def RemoveDup():
	getData(CONST_CLEANED_DATA)

	tempdict = {}
	for i in data:
		tempdict[str(i)] = 1

	with open(CONST_DATA_NO_DUP, "w", encoding = 'UTF-8') as writeFile:
		for keys in tempdict.keys():
			writeFile.write(str(keys))
			writeFile.write(str('\n'))

	writeFile.close()


def findMissingData():
	getData(CONST_DATA_NO_DUP)

	faultCnt = 0
	with open(CONST_MISSING_DATA, "w", encoding = 'UTF-8') as writeFile:
		for i in range(len(data) - 1):
			if data[i]['cumthi'] != data[i + 1]['cumthi']:
				continue

			tempvar = int(data[i + 1]['SBD']) - int(data[i]['SBD'])
			if tempvar == 1:
				continue

			faultCnt += tempvar - 1
			for j in range(int(data[i]['SBD']) + 1, int(data[i + 1]['SBD'])):
				if (len(str(j)) < 8):
					writeFile.write('0' + str(j))
				else:
					writeFile.write(str(j))
				writeFile.write(str('\n'))

	writeFile.close()
	print("Number of missing data: ", faultCnt)


# This function will get the SBD of the file that listed
# on the line with open.
def getListOfID():
	getData(CONST_DATA_NO_DUP)
	with open("ListOfID2.txt", "w", encoding="utf-8") as writeFile:
		for i in data:
			writeFile.write(i['SBD'])
			writeFile.write("\n")

	writeFile.close()

if __name__ == '__main__':
	CleanUp()
	RemoveDup()
	findMissingData()
	# getListOfID()
