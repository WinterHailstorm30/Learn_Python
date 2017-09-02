import random
randomNumber = ''.join(random.sample('0123456789', 4))
listRandomNumber = list(randomNumber)
print('I have generated a random 4 digit number from 0000-9999. It has no repeating digits. Try to guess it!')
while True:
    numberCorrectInPosition = 0
    numberCorrectNotInPosition = 0
    guessNumber = input('What is your guess? ')
    listGuessNumber = list(guessNumber)
    if guessNumber == randomNumber:
        print('YOU WIN!')
        exit()
    if guessNumber.isdigit():
        if int(guessNumber) > -1 and int(guessNumber) < 10000:
            if len(listGuessNumber) == 4:
                for x in range(0, 4):
                    if listRandomNumber[x] == listGuessNumber[x]:
                        numberCorrectInPosition += 1
                print(str(numberCorrectInPosition) + ' digit(s) correct in position')
                for x in range(0, 4):
                    for y in range(0,4):
                        if x != y and listRandomNumber[x] == listGuessNumber[y]:
                            numberCorrectNotInPosition += 1
                print(str(numberCorrectNotInPosition) + ' digit(s) not correct in position')
            else:
                print('ILLEGAL INPUT')
        else:
            print('ILLEGAL INPUT')
    else:
        print("ILLEGAL INPUT")