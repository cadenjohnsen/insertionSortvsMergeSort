The programs in this folder include:
An insertSort.py program that will sort a given data.txt file using the insertion sort method.
A mergeSort.py program that will sort a given data.txt file using the merge sort method.
An insertTime.py program that will create and sort a given array of size n using the insert sort method.
A mergeTime.py program that will create and sort a given array of size n using the merge sort method.
A makefile used to compile all the above programs with Bash.
A data.txt file used that contains an unknown number of lines with unsorted numbers; the first of which is the amount of numbers on the line.

To Compile and Run:
chmod +x makefile
./makefile
./insertSort.py
./mergeSort.py
./insertTime.py
./mergeTime.py

OR

python3 insertSort.py
python3 mergeSort.py
python3 insertTime.py
python3 mergeTime.py

After Execution:
insertSort.py will create an insert.txt file that will contain the data from data.txt sorted using as insertion sort.
mergeSort.py will create an merge.txt file that will contain the data from data.txt sorted using as merge sort.
insertTime.py will run an insert sort on a dataset of a given size n and return the size and execution time.
mergeTime.py will run a merge sort on a dataset of a given size and return the size and execution time.
