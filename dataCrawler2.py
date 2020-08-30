import requests
from bs4 import BeautifulSoup
from threading import Thread
import time
import multiprocessing as mp

CONST_START = 4651275
CONST_STEP = 5
CONST_PROCESSES = 100
CONST_URL = "https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2020&sbd="

def ExtractData(URL, SBD):
	r = requests.get(URL)
	soup = BeautifulSoup(r.text, "html.parser")

	results_container = soup.tbody
	header_container = soup.thead
	header = []
	results = []
	if header_container is None:
		return

	for i in header_container.find_all('th'):
		header.append(i.get_text())

	del header[3]
	del header[3]

	for i in results_container.find_all('td'):
		results.append(i.get_text())

	temp_dict = {}
	temp_dict['SBD'] = SBD

	for i in range(len(results)):
		if (results[i] == ''):
			continue
		temp_dict[str(header[i])] = results[i]

	with open("temp.txt", "a", encoding = 'utf-8') as writeFile:
		writeFile.write(str(temp_dict))
		writeFile.write(str('\n'))

	writeFile.close()

def ExtractFromList(i):
	path = "ListOfID.txt"
	file = open(path, "r", encoding = "UTF-8")
	contents = file.readlines()
	file.close()
	for j in range(i * CONST_STEP, (i + 1) * CONST_STEP):
		contents[j] = contents[j][:-1]
		print("Getting ", contents[j])
		ExtractData(CONST_URL + contents[j], contents[j])

if __name__ == '__main__':
	ExtractFromList(0)
	# processes = [mp.Process(target=ExtractFromList, args=(i, )) for i in range(CONST_PROCESSES)]

	# for p in processes:
	#     p.start()

	# for p in processes:
	#     p.join()
