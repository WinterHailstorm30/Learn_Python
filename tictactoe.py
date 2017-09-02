reference = '''
Please use the following cell numbers to make your move
The board with numbers looks like this:

  1  |  2  |  3  
-----------------
  4  |  5  |  6  
-----------------
  7  |  8  |  9  

The blank board looks like this:

     |     |     
-----------------
     |     |     
-----------------
     |     |     
'''
board = '''
     |     |     
-----------------
     |     |     
-----------------
     |     |     
'''
spread = list(board)
print(reference)
for x in range(0, 9):
    turnX = int(input('Where would you like to place X (1-9)? '))
    if turnX == 1:
        spread[3] = 'X'
    elif turnX == 2:
        spread[9] = 'X'
    elif turnX == 3:
        spread[15] = 'X'
    elif turnX == 4:
        spread[39] = 'X'
    elif turnX == 5:
        spread[45] = 'X'
    elif turnX == 6:
        spread[51] = 'X'
    elif turnX == 7:
        spread[75] = 'X'
    elif turnX == 8:
        spread[81] = 'X'
    elif turnX == 9:
        spread[87] = 'X'
    print(''.join(spread))
    if spread[3] == 'X' and spread[9] == 'X' and spread[15] == 'X':
        print("X Wins")
        exit()
    elif spread[3] == 'X' and spread[39] == 'X' and spread[75] == 'X':
        print("X Wins")
        exit()
    elif spread[3] == 'X' and spread[45] == 'X' and spread[87] == 'X':
        print("X Wins")
        exit()
    elif spread[9] == 'X' and spread[45] == 'X' and spread[81] == 'X':
        print("X Wins")
        exit()
    elif spread[15] == 'X' and spread[51] == 'X' and spread[87] == 'X':
        print("X Wins")
        exit()
    elif spread[15] == 'X' and spread[45] == 'X' and spread[75] == 'X':
        print("X Wins")
        exit()
    elif spread[39] == 'X' and spread[45] == 'X' and spread[51] == 'X':
        print("X Wins")
        exit()
    elif spread[75] == 'X' and spread[81] == 'X' and spread[87] == 'X':
        print("X Wins")
        exit()

    for o in range(0, 1):
        turnO = int(input('Where would you like to place O (1-9)? '))
        if turnO == 1:
            spread[3] = 'O'
        elif turnO == 2:
            spread[9] = 'O'
        elif turnO == 3:
            spread[15] = 'O'
        elif turnO == 4:
            spread[39] = 'O'
        elif turnO == 5:
            spread[45] = 'O'
        elif turnO == 6:
            spread[51] = 'O'
        elif turnO == 7:
            spread[75] = 'O'
        elif turnO == 8:
            spread[81] = 'O'
        elif turnO == 9:
            spread[87] = 'O'

        print(''.join(spread))
        if spread[3] == 'O' and spread[9] == 'O' and spread[15] == 'O':
            print("O Wins")
            exit()
        elif spread[3] == 'O' and spread[39] == 'O' and spread[75] == 'O':
            print("O Wins")
            exit()
        elif spread[3] == 'O' and spread[45] == 'O' and spread[87] == 'O':
            print("O Wins")
            exit()
        elif spread[9] == 'O' and spread[45] == 'O' and spread[81] == 'O':
            print("O Wins")
            exit()
        elif spread[15] == 'O' and spread[51] == 'O' and spread[87] == 'O':
            print("O Wins")
            exit()
        elif spread[15] == 'O' and spread[45] == 'O' and spread[75] == 'O':
            print("O Wins")
            exit()
        elif spread[39] == 'O' and spread[45] == 'O' and spread[51] == 'O':
            print("O Wins")
            exit()
        elif spread[75] == 'O' and spread[81] == 'O' and spread[87] == 'O':
            print("O Wins")
            exit()
        else:
            print("no winner yet")