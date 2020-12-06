
#only for Part 1 of day 3

#open file
forestFile=open(('/home/anjab/PycharmProjects/AdventofCode/venv/numbers.txt'), 'r')
forestList=forestFile.readlines()

treeCount=0

#skip first line
#second line: index 3 check which character, if #, treeCount+1
#next line: index 3+3 check which character
index=0
lineCount=0
for forestString in forestList:

    for i in range(5):
        forestString=forestString.rstrip('\r\n')+forestString.rstrip('\r\n')
    #skip first line
    if(index==0):
        index=3
        continue
    try:
        if(forestString[index]== '#'):
            treeCount=treeCount+1
    except:
        break

    index=index+3
    lineCount=lineCount+1
    if(lineCount==323):
        break

print(treeCount)


#Part 2 of Day 3, to concerns slope Right 1, Down 2. For the other slopes, change the indexes in the above code snippet (line 21 and 29)
index=1
lineCount=0

for forestString in forestList:
    lineCount=lineCount+1
    if(lineCount<=2 or lineCount%2==0):
        continue

    for i in range(5):

        forestString=forestString.rstrip('\r\n')+forestString.rstrip('\r\n')

    try:
       
        if(forestString[index]== '#'):
            treeCount=treeCount+1

    except:
        break

    index=index+1
    if (lineCount == 323):
        break

print(treeCount)
