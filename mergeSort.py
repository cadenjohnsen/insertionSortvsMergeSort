#!/usr/bin/env python3

# function that executes a merge sort with a given array of numbers
def mergesort(words):
	i, j, k = 0, 0, 0
	if (len(words) > 1):
		start = words[:len(words)//2]	# divide the words array in half and store the first half into a start side array
		end = words[len(words)//2:]	# divide the words array in half and store the second half into an end side array

		mergesort(start)	# recursively go into the sort function until the start array has a size of 1
		mergesort(end)		# recursively go into the sort function until the end array has a size of 1

		while i < len(start) and j < len (end):	# check if the current array is not empty yet
			if start[i] < end[j]:		# check if the start array value is smaller than end
				words[k] = start[i]	# replace original array at index k with the start value
				i += 1			# increment i
			else:				# if the end is larger or equal to the start then replace it in the array
				words[k] = end[j]	# replace words at index k with the end value
				j += 1			# increment j
			k += 1				# increment k

		while i < len(start):		# loop through every element in the start array and store them into the words array
			words[k] = start[i]	# add the start array into the words array for each position
			i += 1			# increment i
			k += 1			# increment k

		while j < len(end):		# loop through every element in the end array and store them into the words array
			words[k] = end[j]	# add the end array into the words array for each position
			j += 1			# increment j
			k += 1			# increment k

# function to create the merge.txt file where the answer will be output
def createOutputFile():
	file = open("merge.txt", "w+")		# check if an merge.txt file exists, if not then create one
	file.close()	# close the file without editing

# function to output the sorted words into insert.txt
def writeOutputFile(words, end):
	i = 0
	file = open("merge.txt", "a+")		# opens the file to place the sorted array
	while (i < end):				# loop through every element
		file.write("%s " %str(words[i]))	# convert the numbers back to strings
		i += 1					#increment i
	file.write("\n")	# add a new line character to the end of the file
	file.close()		# close the file after editing is completed

# function to read in the data from data.txt and output it to a matrix
def readData():
	with open("data.txt") as file:		# opens the text file to be read
		i,j = 0, 0
		data = file.readlines()	# reads the text file line by line
		for line in data:	# loops through each line
			words = list(map(int, line.split()))	# converts chars into ints and puts into array
			intsum = words.pop(0)	# removes the first number giving the length of the array

			mergesort(words)		# calling the function that sorts each group
			writeOutputFile(words, intsum)

# function to call and execute other functions
def main():
	createOutputFile()
	readData()

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()
