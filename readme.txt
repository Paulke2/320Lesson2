first, main asks for input for the name of a text file that contains number data, an array of strings
is then created and each line from the user specified .txt file is read into a different index. Then
addNums is called with the new string array containing the lines of the text file as a parameter for
addNums. first, addNums checks the length of the list of data, and if the length is 0, meaning empty,
the string "EMPTY" is returned, else, sumNums is called with a parameter of the array except for the
first index as the first index just specifies the length and is not apart of the data we are summing.
sumNums has an int variable that represents the total count of the data. then there is a for loop that \
loops through or data, and if -999 is encountered, which represents the end of our data, we break out of
the loop and return the total. else, each index greater than 0, will be added to total and once the
end of the array is reached, total will be returned

Run time:
Worst case is O(N)
if -999 is not encountered until the last index or not in our data set, we must loop through all of
our data in the array

Best Case (1)
if the data array is empty, we do not have to run through any data.
