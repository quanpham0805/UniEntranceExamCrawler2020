import ast

CONST_FILE_1_PATH = "newtemp.txt"
CONST_FILE_2_PATH = "temp.txt"
CONST_CUMTHI = "CumThi.txt"
data = []
cumthi = []

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

def getCumThi(path):
	file = open(path, "r", encoding = "UTF-8")
	contents = file.readlines()
	file.close()
	for i in contents:
		cumthi.append(i[:-1])

def formatter(path):
	for i in data:
		if 'Ngoại ngữ' in i:
			i['Ngoại ngữ'] = i['Ngoại ngữ'][3:]

		if 'GDCD' in i:
			i['Giáo dục công dân'] = i['GDCD']
			del i['GDCD']

		if 'Văn' in i:
			i['Ngữ văn'] = i['Văn']
			del i['Văn']

		index = int(i['SBD'][:2]) - 1
		i['cumthi'] = cumthi[index]

	with open(path, "w", encoding = 'UTF-8') as writeFile:
		for i in data:
			writeFile.write(str(i))
			writeFile.write(str('\n'))

	writeFile.close()

if __name__ == '__main__':
	getData(CONST_FILE_2_PATH)
	getCumThi(CONST_CUMTHI)
	formatter(CONST_FILE_1_PATH)