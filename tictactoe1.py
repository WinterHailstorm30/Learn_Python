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
turn = 0
for x in range(0, 9):
    turn = turn + 1
    if turn % 2 == 0:
        piece = 'O'
    else:
        piece = 'X'
    turnX = int(input('Where would you like to place ' + piece + ' (0, 9)?'))
    if turnX == 1:
        spread[3] = piece
    elif turnX == 2:
        spread[9] = piece
    elif turnX == 3:
        spread[15] = piece
    elif turnX == 4:
        spread[39] = piece
    elif turnX == 5:
        spread[45] = piece
    elif turnX == 6:
        spread[51] = piece
    elif turnX == 7:
        spread[75] = piece
    elif turnX == 8:
        spread[81] = piece
    elif turnX == 9:
        spread[87] = piece
    print(''.join(spread))
    if spread[3] == piece and spread[9] == piece and spread[15] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[3] == piece and spread[39] == piece and spread[75] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[3] == piece and spread[45] == piece and spread[87] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[9] == piece and spread[45] == piece and spread[81] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[15] == piece and spread[51] == piece and spread[87] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[15] == piece and spread[45] == piece and spread[75] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[39] == piece and spread[45] == piece and spread[51] == piece:
        print(piece + " Wins!")
        exit()
    elif spread[75] == piece and spread[81] == piece and spread[87] == piece:
        print(piece + " Wins!")
        exit()
        if turn == 9:
            print("the result is a tie")