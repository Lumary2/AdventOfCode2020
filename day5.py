import math

ticketFile=open(('/home/anjab/PycharmProjects/AdventofCode/venv/passports.txt'), 'r')
file=ticketFile.readlines()

rangeLowRow=0
rangeHighRow=127

rangeLowCol=0
rangeHighCol=7
row=0
col=0

listOfTickets=[]
#loop through tickets
for ticket in file:


    #loop through chars of ticket
    countRow=0
    countCol=2
    for element in ticket:

        if(rangeHighRow==rangeLowRow):
            row=rangeHighRow

        if(element=="F" and countRow==0):
            rangeLowRow=0
            rangeHighRow=63
            countRow= countRow + 1
            continue

        if (element == "B" and countRow==0):
            rangeLowRow = 64
            rangeHighRow = 127
            countRow = countRow + 1
            continue

        if(element=="F" and countRow>0):
           rangeLowRow=rangeLowRow
           rangeHighRow= rangeHighRow - int(math.ceil((rangeHighRow - rangeLowRow) / 2))

        if(element=="B" and countRow>0):
           rangeHighRow=rangeHighRow
           rangeLowRow= rangeLowRow + int(math.ceil((rangeHighRow - rangeLowRow) / 2))

        if (element == "L" and countCol == 0):
            rangeLowCol = 0
            rangeHighCol = 3
            countCol = countCol + 1
            continue

        if(rangeHighCol==rangeLowCol):
            col=rangeHighCol
            id=row*8+col
            listOfTickets.append(id)
            rangeHighCol=7
            rangeLowCol=0
            rangeHighRow=127
            rangeLowCol=0
            break

        if (element == "R" and countCol == 0):
            rangeLowCol = 4
            rangeHighCol = 7
            countCol = countCol + 1
            continue

        if (element == "L" and countCol > 0):
            rangeLowCol = rangeLowCol
            rangeHighCol = rangeHighCol - int(math.ceil((rangeHighCol - rangeLowCol) / 2))

        if (element == "R" and countCol > 0):
            rangeHighCol = rangeHighCol
            rangeLowCol = rangeLowCol + int(math.ceil((rangeHighCol - rangeLowCol) / 2))

listOfTickets.sort()

number=7
for element in listOfTickets:

    if(element!=number):
        print("myID "+""+str(element-1))
        break
    number=number+1
