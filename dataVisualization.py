# You have to have python knowledge to use this file. Good luck

import matplotlib.pyplot as plt
import ast
from itertools import combinations

path = "CleanedDataAfterFirstPatch.txt"
file = open(path, "r", encoding = "UTF-8")
contents = file.readlines()
file.close()


# {'SBD': '01000002', 'cumthi': 'Cụm thi: 01 - Sở GDĐT Hà Nội', 'Toán': '9.00', 'Ngữ văn': '6.00', 'Ngoại ngữ': '9.40', 'Vật lý': '7.25', 'Hóa học': '8.75', 'Sinh học': '7.25'}

# data variable is a list of dictionary
# ['SBD']
# ['cumthi']
# ['Subject 1']
# ['Subject 2']
# ['Subject 3']
# ['Subject 4']
# ['Subject 5']
# ['Subject 6']

data = [ast.literal_eval(row) for row in contents]
list_kh = ['Toán', 'Ngữ văn', 'Ngoại ngữ', 'Vật lý', 'Hóa học', 'Sinh học', 'Lịch sử','Địa lý', 'Giáo dục công dân']
# list_khtn = ['Toán', 'Ngữ văn', 'Ngoại ngữ', 'Vật lý', 'Hóa học', 'Sinh học']
# list_khxh = ['Toán', 'Ngữ văn', 'Ngoại ngữ', 'Lịch sử','Địa lý', 'Giáo dục công dân']
list_combination = []
dataByFac = {}

def getCombination():
	comb = combinations([0, 1, 2, 3, 4, 5, 6, 7, 8], 3)
	for i in list(comb):
		list_combination.append(i)

def getCombinedMarksWithoutAvg(id):
	cumthi = "Cụm thi: 28 - Sở GDĐT Thanh Hoá"
	if not id in dataByFac:
		dataByFac[id] = {}

	for i in data:
		if not list_kh[list_combination[id][0]] in i or not list_kh[list_combination[id][1]] in i or not list_kh[list_combination[id][2]] in i or i['cumthi'] != cumthi:
			continue

		score = float(i[list_kh[list_combination[id][0]]]) + float(i[list_kh[list_combination[id][1]]]) + float(i[list_kh[list_combination[id][2]]])
		score = round(score, 2)
		if not score in dataByFac[id]:
			dataByFac[id][score] = 0
		dataByFac[id][score] += 1

def getCombinedMarksWithAvg(id):
	pass

def getCombinedMarks(id):
	# if list_combination[id][0] != 6 and list_combination[id][1] != 6 and list_combination[id][2] != 6:
	getCombinedMarksWithoutAvg(id)
	# else:
	# 	getCombinedMarksWithAvg(id)


def makeGraph(id):
	point = []
	count = []
	const_start = 26
	const_increment = 0.25
	totalStudents = 0
	i = 0;
	while const_start + i * const_increment < 30:
		total = 0
		for key in sorted(dataByFac[id].keys()):
			if float(const_start + i * const_increment) < key and key <= float(const_start + (i + 1) * const_increment):
				total += dataByFac[id][key]

		point.append(str(const_start + i * const_increment) + '\n|\n' + str(const_start + (i + 1) * const_increment))
		count.append(total)
		totalStudents += total
		i += 1

	print(totalStudents)
	plt.title("Số thí sinh theo tổng điểm " + list_kh[list_combination[id][0]] + ' + ' + list_kh[list_combination[id][1]] + ' + ' + list_kh[list_combination[id][2]])
	plt.xlabel('Số điểm')
	plt.ylabel('Lượng học sinh')
	rects = plt.bar(point, count, alpha=0.5, width=0.7, tick_label=point)

	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x() + rect.get_width()/2., height + 1, height, ha='center', va='bottom')

	plt.show()


if __name__ == '__main__':
	getCombination()
	# print(list_combination)
	getCombinedMarks(18)
	makeGraph(18)
	# for i in range(len(list_combination)):
	# 	getCombinedMarks(i)
	# 	makeGraph(i)