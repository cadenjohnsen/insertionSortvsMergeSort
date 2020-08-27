#!/usr/bin/env python3

from random import randint	# needed to create random numbers
import timeit	# needed to use timer function

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

# function to create a random array of size n
def createArray(words, n):
	i = 0
	for i in range(0,n):			# go through all numbers in the set
	    value = randint(0,10000)	# create a random integer between 0 and 10000
	    words.insert(i, value)		# store that random int within the words list
	mid = n / 2	# gets the midpoint of the line
	end = n		# gets the end of the line

# function to call and execute other functions
def main():
	n = 1000
	words = []		# declare the initially empty words array
	createArray(words, n)	# store returned values into variables
	start = timeit.default_timer()	# begins the timer setting it with system clock value
	mergesort(words)			# calling the function that sorts each group
	stop = timeit.default_timer()	# ends the timer with the system clock value
	time = stop - start	# calculate the difference between start and stop for the total time of execution

	print("Size: ", n)	# displays size of array that was sorted
	print('Time: ', time, 'sec')	# displays the time taken for execution

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()
