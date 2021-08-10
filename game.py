#-*-coding: utf-8-*-

import sys

def main(filename):

        dataFile = open(filename, 'r')          #Open input file
	outFile = open(filename + '.out', 'w')  #Open output file
	tripFlag = 0                            #State flag for each trip
	pplnumber = 0				#Set the number of people in each trip
	sumCounter = 0				#The number of contributions
	sum = 0					#Sum of each persons contributions
	totalSum = 0				#The total amount of money in the pool
	totalAvg = 0				#Total average per person
	resultList=[]				#Results per each person

	for ln in dataFile:			#Go thru all the file

		if ln ~= '':			#Ignore blank spaces

			if ln == 0:		#The end of the trip
				totalAvg = totalSum / pplnumber #Get average
				for numb in resulList:
					outFile.write(totalAvg-numb) #Print into file each difference from average vs contributions
					print(totalAvg-numb)	     #Print to console

			if tripFlag == 0:			     #Know which line is being read 1st to set number of people
				pplnumber == ln
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
				else:					#Save the result and add it to list
					resultList.append(sum)          #Save sum for each person
					sum = 0
					i = 0
					tripFlag = 1

	dataFile.close()	#Files to be closed
	outFile.close()

if __name__ == "__main__":
	main(sys.argv)
