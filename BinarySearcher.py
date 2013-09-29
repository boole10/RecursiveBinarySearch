import os
#reads the names from the file into a list
def readNames():
	dirname, filename = os.path.split(os.path.abspath(__file__))
	inputFile = open(dirname + "/sorted.txt","r")
	word = ""
	done = False 
	while not done:
		word = chop(inputFile.readline())
		if not word:
			done = True
		else:
			list.append(word)
		#appends the chopped version of the line(without a \n)
	inputFile.close()
			
			
#removes the newline at then of every string if it exists.
def chop(word):
	if "\n" in word:
		word = word[:len(word) -1]
	return word	
def getword():
	word = raw_input("Enter the word to search for: ")
	return word
def binarySearch(first,second):
	middleNum = (first+second)/2
	if first > second:
		return (False,-1)
	else:
		if word == list[middleNum]:
			return (True, middleNum)
		elif word > list[middleNum]:
			return binarySearch(middleNum+1,second)
		elif word < list[middleNum]:
			return binarySearch(first,middleNum-1)
#sorts everything, first reading in names
list = []
readNames()
word = getword()
found,pos = binarySearch(0,len(list))
if found:
	print "The word was found at position " + str(pos) + "in the list"
else:
	print "The word wasn't found"
