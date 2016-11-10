#Random Name Generator by Ian Guitard
import random
vowels = ["a", "e", "i", "o", "u", "y", "oo", "ee", "ae", "ai", "ao", "au", "ea", "eo", "eu", "ei", "ia", "ie", "io", "iu", "oa", "oi", "ou", "oe"]
consonants = ["b", "bw", "c", "d", "f", "fw", "g", "gw", "h", "hw", "j", "k", "kw", "l", "m", "mw", "n", "p", "pw", "q", "r", "s", "sw", "t", "tw", "v", "w", "x", "y", "z", "bl", "br", "cl", "cr", "dr", "fl", "fr", "gl", "gr", "hr", "kl", "kr", "ng", "pl", "pr", "qu", "sl", "sr", "st", "str", "tr", "ts", "vl", "wr"]
def randomName():
    length = random.randint(2, 10)
    nameVowelNumber = []
    nameConsonantNumber = []
    for x in range(0, (length - 2)):
        if (x + 2) % 2 == 1:
            nameVowelNumber.append([x])
        elif (x + 2) % 2 == 0:
            nameConsonantNumber.append([x])
    y = 0
    nameVowels = []
    while y <= len(nameVowelNumber):
        z = random.randint(0, (len(vowels) - 1))
        nameVowels.append(vowels[z])
        y += 1
    y = 0
    nameConsonants = []
    while y <= (len(nameConsonantNumber) - 1):
        z = random.randint(0, (len(consonants) -1))
        nameConsonants.append(consonants[z])
        y += 1
    y = 0
    name = []
    while y < ((len(nameConsonants) - 1)):
        name.append(nameConsonants[y])
        name.append(nameVowels[y])
        y += 1
    if not name:
        w = random.randint(6, (len(vowels) - 1))
        name.append(vowels[w])
##    print(nameVowels)
##    print(nameConsonants)
##    print(nameVowelNumber)
##    print(nameConsonantNumber)
##    print(name)
    print("".join(name))
while True:
    randomName()
    exitCondition = input()
    if "quit" in exitCondition:
       quit()
