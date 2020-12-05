
#loop through all the passwords. In each line we need to split up the line like this:
#(1)(-)(22)(k)(:)(kkkk)
#store index values 0,2,3 and 5 each in separate variables
#count number of characters in password
#check if number of character in string is at least minimum value and not > max. value

#open file with passwords
passwordFile=open(('/home/anjab/PycharmProjects/AdventofCode/venv/numbers.txt'), 'r')
passwordList=passwordFile.readlines()

validCount=0
for password in passwordList:
     passwordsElements=password.split()

     numbers=passwordsElements[0].split('-')
     numberMin=int(numbers[0])
     numberMax=int(numbers[1])

     character=passwordsElements[1][0]
     password=passwordsElements[2]

#Part One of Advent of Code Day2
     #numberOccurence=int(password.count(character))

     #if(numberOccurence>=numberMin and numberOccurence<=numberMax):
      #      validCount=validCount+1

#Part Two AfC Day2
     if(password[numberMin-1]==character and password[numberMax-1]!=character):
        validCount=validCount+1
     if (password[numberMin - 1] != character and password[numberMax - 1] == character):
        validCount = validCount + 1

print(validCount)