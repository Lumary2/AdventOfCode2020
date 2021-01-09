import re

passportFile=open(('/home/anjab/PycharmProjects/AdventofCode/venv/passports.txt'), 'r')
file=passportFile.read()

separatedPassports=file.split('\n\n')

validPassportCount= 0

def checkValidity(regex, passportElements):
    if (regex==r"(cid.*)"):
        return True
    elif (regex==r"(byr.*)"):
        if(int(passportElements[1])>=1920 and int(passportElements[1])<=2002):
            return True
    elif (regex==r"(pid.*)"):
        if(len(passportElements[1])==9):
            print(passportElements[1])
            return True
    elif (regex==r"(eyr.*)"):
        if(int(passportElements[1])>=2020 and int(passportElements[1])<=2030):
            return True
    elif (regex==r"(hcl.*)"):
        if((bool(re.search(r'[#]{1}[0-9|a-f]{6}', passportElements[1])))==True):
            return True
    elif (regex==r"(iyr.*)"):
        if(int(passportElements[1])>=2010 and int(passportElements[1])<=2020):
            return True
    elif (regex==r"(hgt.*)"):
        separateHeight=re.split(r'(\d+)', passportElements[1])

        if(separateHeight[2]=='cm'):
            if(int(separateHeight[1])>=150 and int(separateHeight[1])<=193):
                return True
        elif (separateHeight[2] == 'in'):
            if (int(separateHeight[1]) >= 59 and int(separateHeight[1]) <= 76):
                return True

    elif (regex==r"(ecl.*)"):
        if(bool(re.search(r'amb|blu|brn|gry|grn|hzl|oth', passportElements[1]))==True):
            return True
    else:
        return False

#Part One AoC Day 4
for passport in separatedPassports:


    regexArray=[r"(cid.*)",r"(byr.*)",r"(pid.*)",r"(eyr.*)",r"(hcl.*)",r"(iyr.*)",r"(hgt.*)",r"(ecl.*)"]

    CountPWElements=0
    validElementCount=0
    for regex in regexArray:
        if ((bool(re.search(regex, passport)))==True):
            CountPWElements= CountPWElements + 1
            element=re.search(regex,passport).group(1)

            deleteBlanks=element.split(' ')
            passportElements=deleteBlanks[0].split(':')

            validElement=checkValidity(regex,passportElements)

            if(validElement==True):
                validElementCount=validElementCount+1

    if(validElementCount==8 and CountPWElements==8):

        validPassportCount= validPassportCount + 1
    if(validElementCount==7 and CountPWElements==7 and (bool(re.search(r"(cid.*)", passport)))==False):
        validPassportCount = validPassportCount + 1



print(validPassportCount)
