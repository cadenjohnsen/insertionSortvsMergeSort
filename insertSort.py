#!/usr/bin/env python3

# function that executes an insertion sort with a given array of numbers
def insertsort(words, start, mid, end):
	i, j = 0, 0
	for i in range(1, end):		# loops through all numbers in a row
		index = words[i]	# creates a current index variable and sets its contents to the current word
		j = i - 1	# adds a second variable to iterate over the words array
		while j >= 0 and index < words[j]:	# loops through and checks if the previous index is nonzero and the current word is less than the previous one
			words[j+1] = words[j]	# if the current word is more than the previous then move the smaller number back in the array
			j-=1	# decrement counter
		words[j+1] = index	# move the current word into the last used slot

# function to create the insert.txt file where the answer will be output
def createOutputFile():
	file = open("insert.txt", "w+")		# check if an insert.txt file exists, if not then create one
	file.close()	# close the file without editing

# function to output the sorted words into insert.txt
def writeOutputFile(words, end):
	i = 0
	file = open("insert.txt", "a+")		# opens the file to place the sorted array
	while (i < end):				# loop through every element
		file.write("%s " %str(words[i]))	# convert the numbers back to strings
		i += 1					#increment i
	file.write("\n")	# add a new line character to the end of the file
	file.close()		# close the file after editing is completed

# function to read in the data from data.txt and output it to a matrix
def readData():
	with open("data.txt") as file:	# opens the data.txt text file to be read
		i, j = 0, 0
		data = file.readlines()	# read the text file line by line
		for line in data:	# loops through each line
			words = list(map(int, line.split()))	# converts chars into ints and put into array
			intsum = words.pop(0)	# removes the first number which gives the length of the array
			start = 0			# initialize start to 0
			if (intsum % 2 == 0):		# checks if the total number of variables is even
				mid = intsum / 2	# gets the midpoint of the line
			else:
				mid = intsum / 2 + 1	# make the midpoint of the line the number after the middle
			end = intsum			# gets the end of the line

			insertsort(words, start, mid, end)	# calling the function that sorts each group
			writeOutputFile(words, end)	# call to function that writes to output file

# function to call and execute other functions
def main():
	createOutputFile()
	readData()

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()
