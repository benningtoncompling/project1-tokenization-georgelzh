import re
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

f = open(inFile, "r", encoding ='UTF-8')
txt = f.read()


#Remove  <...></something>
x = re.sub("<(\/)?\w+(\/)?>", "" , txt)
x = re.sub("<\w+\s.{0,300}\">", "", x)

#remove numbers and symbols
x = re.sub("\d|[=://@!#$%^&*(+{}:\"?>;.,)\[\]\|-]", "", x)
x = re.sub("_", " ", x)
x = re.sub("(\'\')", "", x)
x = x.lower()
x = re.sub("\s+", " ", x)

#make the string into array
x = x.split(" ")

# delete all the empty item
for word in x:
    if word == '':
        x.remove(word)

#create a new dictionary
wordDict = {}

#count the word and make a dictionary

for word in x:
    if word not in wordDict:
        wordDict[word] = 1
    elif word in wordDict:
        wordDict[word] = wordDict[word] + 1

#open a new File
newFile = open(outFile, "a", encoding ='UTF-8')

#print wordDict and store it as a string
for word in wordDict:
    newFile.write(str(wordDict.get(word)) + word + " " + "\n")

#write the result into a new txt
#newFile.write(wordDict)

print(newFile)

#reference
#1. How to convert int to string https://www.techwalla.com/articles/how-to-convert-int-to-string-in-python
