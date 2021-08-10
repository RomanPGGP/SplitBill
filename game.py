#-*-coding: utf-8-*-

import sys

def main(filename):

	dataFile = open(filename[1], 'r')       #Open input file
	outputFilename = filename[1] + '.out'
	outFile = open(outputFilename, 'w')     #Open output file
	tripFlag = 0                            #State flag for each trip
	pplnumber = 1				#Set the number of people in each trip
	sumCounter = 0				#The number of contributions
	sum = 0					#Sum of each persons contributions
	totalSum = 0				#The total amount of money in the pool
	totalAvg = 0				#Total average per person
	resultList=[]				#Results per each person
	i = 0

	for lin in dataFile:			#Go thru all the file

		ln = float(lin)

		if ln != '':			#Ignore blank spaces

			if ln == 0:		#The end of the trip
				totalAvg = totalSum / pplnumber #Get average

				print('total sum:' + str(totalSum))
				print('people number:' + str(pplnumber))
				print('total avg:' + str(totalAvg))
				for numb in resultList:
					print('Money given per person:'+str(numb))
					outFile.write(str(totalAvg-numb)+'\n') #Print into file each difference from average vs contributions
					print(totalAvg-numb)	     #Print to console

			if tripFlag == 0:			     #Know which line is being read 1st to set number of people
				pplnumber = ln
				tripFlag = 1
				continue
			elif tripFlag == 1: 			     #Set number of contributions
				sumCounter = ln
				tripFlag = 2
				continue
			else:					     #Start addition

				if i < sumCounter:		     #Sum if lines are to be added
					sum = sum + ln
					totalSum = totalSum + ln
					i = i + 1
					if i >= sumCounter:
						tripFlag = 1
						resultList.append(sum)
						sum = 0
						i = 0
					else:
						pass

	dataFile.close()	#Files to be closed
	outFile.close()

if __name__ == "__main__":

	main(sys.argv)
