import random
import string


def myRandomString():
    finalList = []
    # printing lowercase
    letters = string.ascii_lowercase
    lowerCase = list(''.join(random.choice(letters)
                             for i in range(random.randint(2, 4))))
    for lowerChar in lowerCase:
        finalList.append(lowerChar)
    # printing uppercase
    letters = string.ascii_uppercase
    upperCase = list(''.join(random.choice(letters)
                             for i in range(random.randint(2, 4))))
    for upperChar in upperCase:
        finalList.append(upperChar)
    # printing digits
    letters = string.digits
    myNumber = list(''.join(random.choice(letters)
                            for i in range(random.randint(2, 4))))
    for randomNumber in myNumber:
        finalList.append(randomNumber)
    random.shuffle(finalList)

    finalList = finalList[0:6]
    finalString = ''.join(finalList)
    return(finalString)


print(myRandomString())
