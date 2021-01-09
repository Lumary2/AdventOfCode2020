from collections import Counter


puzzleInput=open(('/home/anjab/PycharmProjects/AdventofCode/venv/passports.txt'), 'r')
file=puzzleInput.read()

answers=file.split('\n\n')



#Part Two
sumAnswers=0

for answer in answers:

    ansCount=(answer.count("\n")+1)
    answer=answer.replace("\n","")

    charCount=Counter(answer)
    elements=charCount.values()

    for element in elements:
        if(element==ansCount and ansCount!=1):
            sumAnswers=sumAnswers+1
        if (ansCount == 1):
            sumAnswers = sumAnswers + 1
        if(sumAnswers==3640):
            print(sumAnswers)

print(sumAnswers)



#Part One
#sumAnswers=0
#for answer in answers:
#    answer=answer.replace("\n","")

 #   s = set(answer)  # Creates a set of Unique Un-Ordered Elements
  #  l = len(s)

   # sumAnswers=sumAnswers+l

#print(sumAnswers)