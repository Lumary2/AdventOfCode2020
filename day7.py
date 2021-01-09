import re

puzzleInput=open(('/home/anjab/PycharmProjects/AdventofCode/venv/passports.txt'), 'r')
file=puzzleInput.read()

answers=file.split('\n')

colorList=[]
colorList.append("shiny gold")

def getColors(colorList):
    lengthOldList=len(colorList)

    for answer in answers:
            for color in colorList:
        #for color in colorList:
                if ((bool(re.search(color, answer)))):
                    list=answer.split(' ')
                    colorToAppend=list[0]+' '+list[1]

                    if colorToAppend not in colorList:
                                colorList.append(list[0] + ' ' + list[1])

    if(lengthOldList!=len(colorList)):
        getColors(colorList)

getColors(colorList)
print(len(colorList)-1)






