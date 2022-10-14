# Assignment 2
# Radmehr Mehdipour
# This algorithm takes a number of names given by the user and compares how they sound using the soundex algorithm.

def nameList():
    '''
    This function takes a bunch of names given by the user and puts them in the list
    :return: the list of names given by the userInp excluding 'DONE'
    '''
    names = []
    done = True
    userInp = input('Enter names, one on each line. Type DONE to quit entering names.\n')
    names.append(userInp)
    while done: #if done = False, the loop ends.
        userInp = input()
        names.append(userInp)
        if userInp == 'DONE':
            done = False
    return names[:-1]

def soundex(name):
    '''
    This function takes a name and finds its soundex.
    :param name: Each name given from the list
    :return: a tuple consisting of the soundex of the name and the original string.
    '''
    global step6

    def ltrChange(name):
        '''
        This function grabs a name and turns each letter into a specific digit.
        :param name: name given by the user
        :return: digits corresponding to each letter in name
        '''
        name.lower()
        nameLetter = list(name) #turns a parameter into a list.
        newName = []
        list0 = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
        list1 = ['b', 'f', 'p', 'v']
        list2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']
        list3 = ['d', 't']
        list4 = ['l']
        list5 = ['m', 'n']
        list6 = ['r']
        for ltr in nameLetter:
            if ltr in list0:
                newName.append('0')
            elif ltr in list1:
                newName.append('1')
            elif ltr in list2:
                newName.append('2')
            elif ltr in list3:
                newName.append('3')
            elif ltr in list4:
                newName.append('4')
            elif ltr in list5:
                newName.append('5')
            elif ltr in list6:
                newName.append('6')

        translatedList = "".join(newName)

        return translatedList

    def consecutiveDigits(digits):
        '''
        This function takes a look at a bunch of digits and if there are any consecutive repeats, it removes one of the numbers.
        :param digits: string of digits
        :return: string of digits without any consecutive repeats.
        '''
        newDigits = []
        lastVal = 0

        for number in digits:
            if number != lastVal: #if number equals the previous number, this is to check for consecutive repeats
                newDigits.append(number)
                lastVal = number

        return newDigits

    def zeroFunction(partialSound):
        '''
        This function takes a string of digits and removes any 0 in it.
        :param partialSound: string of digits
        :return: string of digits excluding 0's
        '''
        partialSound = list(partialSound)
        while len(partialSound) < 4:
            partialSound.append('0'*1)
        if len(partialSound) > 4:
            partialSound = partialSound[:4]

        partialSound = "".join(partialSound)

        return partialSound

    loweredName = name.lower()

    F = loweredName[0]
    digitF = ltrChange(F)

    step3 = (ltrChange(loweredName))

    step4 = (consecutiveDigits(step3))

    listStep4 = list(step4)
    while '0' in listStep4: #while loop ends when there is no 0 in the list
        listStep4.remove('0')

    step5 = ''.join(listStep4) #joins all the elements of the list into one.

    if len(step5) > 0:
        if step5[0] == digitF:
            secondPart = step5[1:]
            step6 = F + secondPart
        elif step5[0] != digitF:
            step6 = F + step5
    else:
        step6 = F

    soundex = zeroFunction(step6)

    return (soundex, name)

def main():
    namesInList = nameList()
    namesInList.sort()

    listOfOutputs = []
    for names in namesInList:
        Name1 = soundex(names)[1] # stores the value of the name element of the tuple given by the soundex function.
        Soundex1 = soundex(names)[0] # stores the value of the soundex element of the tuple given by the soundex function.

        for names2 in namesInList:
            Name2 = soundex(names2)[1]
            Soundex2 = soundex(names2)[0]

            if (Name1 != Name2) and (Soundex1 == Soundex2):
                listNames = [Name1, Name2]
                firstName = min(listNames)
                secondName = max(listNames)
                listOfOutputs.append(f'{firstName} and {secondName} have the same Soundex encoding.')

    finalOutputs = []
    for output in listOfOutputs:
        if output not in finalOutputs:
            finalOutputs.append(output)

    finalOutputs.sort()

    for statements in finalOutputs:
        print(statements)

main()
