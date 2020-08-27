#!/usr/bin/env python3

from random import randint	# needed to create random numbers
import timeit	# needed to use timer function

# function that executes an insertion sort with a given array of numbers
def insertsort(words, beginning, mid, end):		# function to execute the insert sort
	i,j = 0, 0
	for i in range(1, end):		# loops through from the first number to the last in the line
		index = words[i]		# creates a current variable and sets its contents to the current word
		j = i - 1				# adds a second variable to iterate over the previous variable
		while j >= 0 and index < words[j]:	# loops through and checks if the previous index is nonzero and the current word is less than the previous one
			words[j+1] = words[j]		# if it is true then the move the smaller number back through the array
			j-=1
		words[j+1] = index		# move the current word into the last used slot

# function to create a random array of size n
def createArray(words, n):
	i = 0
	for i in range(0,n):			# go through all numbers in the set
	    value = randint(0,10000)	# create a random integer between 0 and 10000
	    words.insert(i, value)		# store that random int within the words list
	mid = n / 2	# gets the midpoint of the line
	end = n		# gets the end of the line
	return 0, mid, end

# function to call and execute other functions
def main():
	n = 1000
	words = []		# declare the initially empty words array
	beginning, mid, end = createArray(words, n)	# store returned values into variables
	start = timeit.default_timer()	# begins the timer setting it with system clock value
	insertsort(words, beginning, mid, end)	# calling the function that sorts each group
	stop = timeit.default_timer()	# ends the timer with the system clock value
	time = stop - start	# calculate the difference between start and stop for the total time of execution

	print("Size: ", n)	# displays size of array that was sorted
	print('Time: ', time, 'sec')	# displays the time taken for execution

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()
