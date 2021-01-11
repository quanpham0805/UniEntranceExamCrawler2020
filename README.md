# UniEntranceExamCrawler2020


## The University Entrance Exam Crawler Project, 2020

I decided to create this project to practice my Python skills

#### File explanations:
- dataCrawler.py: crawl data from the vnexpress.
- dataCrawler2.py:  crawl data from other site which has the detail of language marks.
- dataProcessor: clean up raw data
- dataVisualization: graphing
- Data2To1Formatter: format data 2 to have the same format as the data1, because I used page 2 to patch data of 1
- findDiff2And1: after getting the id of list of data 1 and 2, compare them and then get the difference
- CleanedDataAfterFirstPatch: the current total data.

#### Folder explanations:
- DataHanoi: as title
	+ MissingData: the data that was neglected by final file
	+ final: the data after clean up from only crawling hanoi data
	+ new: the data after clean up from crawling all students data, but only hanoi

#### Instruction on how to use this folder:
- Follow the file revision order: dataCrawler (to get data) -> dataProcessor (to clean data) -> dataVisualization (for graphing)
- Instructions will be written carefully in each files
- Before running any script review carefully
