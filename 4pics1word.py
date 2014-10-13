# Author : Joy Deep Nath joy@splashmath.com
# Created: Oct 13, 2014

#!/usr/bin/python
import sys
import itertools
dictFile = '/usr/share/dict/web2'

charSet =""
wordLen =0

if (len (sys.argv) <2):
    charSet = raw_input ("Please enter the character Set:")
    wordLen = len(charSet);
else:
    charSet = sys.argv[1]

print "========================================================================"

if (len(sys.argv) == 2):
    wordLen = len(sys.argv[1])
    print "Finding JUMBLED word from - " +  charSet
if (len(sys.argv) ==3):
    wordLen = int(sys.argv[2])
    print "Finding a " + sys.argv[2] + " letter word out of " + sys.argv[1] + " ..."

# Step 1: Importing the Dictionay to a list
with open(dictFile, 'r') as searchfile:
    dictionary = searchfile.readlines()

# Step 2: Removing new line characters - cleaned up dict
dictList = []
for word in dictionary:
    dictList.append(word.rstrip('\n'))


# Step 3: finding all permutations of input 
print "Finding the permutations ...."
jumbledList = list (map ("".join, itertools.permutations (charSet, wordLen)))
jumbledList = list(set(jumbledList))
#jumbledList.sort()

# Step 4: Checking if the jumbled words exist in the dict (Dictionary)
trueWords = []
for item in jumbledList:
    if (item in dictList):
        trueWords.append(item)
trueWords.sort()

# Step 5: Showing them neatly
print "========================================================================"
for word in trueWords:
    print word

print "========================================================================"
print "Total Words found - "+ str(len(trueWords)) + "\n"
