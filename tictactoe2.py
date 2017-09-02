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

def finalResult(message):
    print(message)
    exit()

checkList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(0, 9):
    turn = turn + 1
    if turn % 2 == 0:
        piece = 'O'
    else:
        piece = 'X'
    while True:
        turnPiece = int(input('Turn ' + str(turn) + ': Where would you like to place ' + piece + ' (1, 9)? '))
        if checkList[turnPiece - 1] == 1:
            print("ILLEGAL INPUT: PLEASE TRY AGAIN")
        else:
            checkList[turnPiece - 1] = 1
            if turnPiece < 10 and turnPiece > 0:
                break
            else: 
                print("ILLEGAL INPUT: PLEASE TRY AGAIN")
    pieceIndexList = [3, 9, 15, 39, 45, 51, 75, 81, 87]
    position = pieceIndexList[turnPiece - 1]
    spread[position] = piece
    print(''.join(spread))
    if spread[3] == piece and spread[9] == piece and spread[15] == piece:
        finalResult(piece + " Wins!")
    elif spread[3] == piece and spread[39] == piece and spread[75] == piece:
        finalResult(piece + " Wins!")
    elif spread[3] == piece and spread[45] == piece and spread[87] == piece:
        finalResult(piece + " Wins!")
    elif spread[9] == piece and spread[45] == piece and spread[81] == piece:
        finalResult(piece + " Wins!")
    elif spread[15] == piece and spread[51] == piece and spread[87] == piece:
        finalResult(piece + " Wins!")
    elif spread[15] == piece and spread[45] == piece and spread[75] == piece:
        finalResult(piece + " Wins!")
    elif spread[39] == piece and spread[45] == piece and spread[51] == piece:
        finalResult(piece + " Wins!")
    elif spread[75] == piece and spread[81] == piece and spread[87] == piece:
        finalResult(piece + " Wins!")
    if turn == 9:
        finalResult("the result is a tie")