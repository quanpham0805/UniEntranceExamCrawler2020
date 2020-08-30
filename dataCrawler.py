#########################################################################################
# Instruction:
# Modify only the constant values as instructed
# run the code by navigating the cmd to the folder of this file, then type
# python dataCrawler.py
#########################################################################################

import requests
from bs4 import BeautifulSoup
from threading import Thread
import time
import multiprocessing as mp


# start of the index of the results page.
CONST_START = 4651275

# number of concurrent processes
# ryzen 9 3900X can handle 500 processes at a time with 30% CPU used.
# For normal machine < 50 is recommended
CONST_PROCESSES = 100

# how many time each process is going to run
CONST_STEP = 80

# the link to the result page
CONST_URL = "https://diemthi.vnexpress.net/index/detail/id/"

# the file destination path
CONST_DATA_PATH = "newData.txt"

#########################################################################################
# Do not modify the code below unless you know exactly what you are doing
#########################################################################################

def ExtractData(URL):
	r = requests.get(URL)
	soup = BeautifulSoup(r.text, "html.parser")

	info = soup.find('p', attrs = {'class': 'o-detail-thisinh__cumthi'})
	results_container = soup.find('div', attrs = {'class':'o-detail-thisinh__diemthi'})
	results = []
	if results_container is None:
		return

	for i in results_container.find_all('td'):
		results.append(i.get_text().strip())

	results.pop()

	cumthi = info.get_text().strip()
	sbd = soup.find('h2', attrs = {'class': 'o-detail-thisinh__sbd'}).strong.get_text().strip()

	temp_dict = {}
	temp_dict['SBD'] = sbd
	temp_dict['cumthi'] = cumthi
	for i in range(int(len(results) / 2)):
		temp_dict[results[i * 2]] = results[i * 2 + 1]
	with open(CONST_DATA_PATH, "a", encoding = 'utf-8') as writeFile:
		writeFile.write(str(temp_dict))
		writeFile.write(str('\n'))

	writeFile.close()

def extractUsingStep(i):
	for j in range(CONST_START + i * CONST_STEP, CONST_START + (i + 1) * CONST_STEP):
		print("Getting ", j, 'at: ', str(int(time.time())))
		ExtractData(CONST_URL + str(j))


if __name__ == '__main__':

	with open(CONST_DATA_PATH, "w", encoding = 'utf-8') as writeFile:
		print("deleting old files...")
	writeFile.close()
	print("done")

	# processes = [mp.Process(target=extractUsingStep, args=(i, )) for i in range(CONST_PROCESSES)]

	# for p in processes:
	#     p.start()

	# for p in processes:
	#     p.join()
