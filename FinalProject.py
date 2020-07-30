import time
import random
print("WELCOME TO TIC TAC TOE")
time.sleep(0.2)
def intro():
    print("What is the name of player 1?")#Intro
    player1 = input()
    player1 = player1.upper()
    time.sleep(0.5)
    print("What is the name of player 2?")
    player2 = input();
    player2 = player2.upper()
    time.sleep(0.5)

    randomNumber = random.randint(1,2)#Picks Xs and Os randomly
    if str(randomNumber) =='1':
        print( player1 + " is X. " + player2 + " is O.")
    else:
        print( player2 + " is X. " + player1 + " is O.")
    time.sleep(1.5)
def switchPlayersIntext(person):
        print("It's your turn," + person + ".Which place would you like to move to?")
        if person == 'X':
                return person == 'O'
        else:
                return person == 'X'
class Player:
    
    def __init__(self, type):
        
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)

class Board:
    

    def __init__(self):
     
        self.board = {
            '1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

    def ifSpaceOpen(self, position):
        if self.board[position] == " ":
            return True
        else:
            return False
    def print_board(self):
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])

    def isThereWinner(self, player):
    
        if self.board["1"] == player.type and self.board["2"] == player.type and self.board["3"] == player.type or self.board["4"] == player.type and self.board["5"] == player.type and self.board["6"] == player.type or self.board["7"] == player.type and self.board["8"] == player.type and self.board["9"] == player.type or self.board["1"] == player.type and self.board["4"] == player.type and self.board["7"] == player.type or self.board["2"] == player.type and self.board["5"] == player.type and self.board["8"] == player.type or self.board["3"] == player.type and self.board["6"] == player.type and self.board["9"] == player.type or self.board["1"] == player.type and self.board["5"] == player.type and self.board["9"] == player.type or self.board["7"] == player.type and self.board["5"] == player.type and self.board["3"] == player.type:
            return True
        return False

    def change_board(self, position, type):
        if self.ifSpaceOpen(position):
            self.board[position] = type
            return self.board
        return None



class Game:

    def __init__(self):
        
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def change_board(self, position, type):
        if self.board.change_board(position, type) is not None:
            return self.board.change_board(position, type)
        else:
            print("That position is already filled. Try another")
            position = input()
            return self.board.change_board(position, type)
    def switchPlayers(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1
    def drawingBoard(self):
       
        self.board.print_board()



    def isThereWinner(self, player):
        return self.board.isThereWinner(player)


    def printPossibleMoves(self):
        
        print("""
            1 - top left    | 2- top middle    | 3 - top right
            4 - middle left | 5 - center        | 6 - middle right
            7 - bottom left | 8 - bottom middle | 9 - bottom right""")


def play():
    TicTacToe = Game()
    TicTacToe.printPossibleMoves()
    player = TicTacToe.player1
    filledSpaces = 0
    while True:    
        while True:
            filledSpaces = filledSpaces + 1
            switchPlayersIntext('X')
       
            TicTacToe.drawingBoard()
            position = input()
            TicTacToe.change_board(position, player.type)
        
            if TicTacToe.isThereWinner(player):
                time.sleep(3)
                print("{} is the Winner!".format(player))
                break
            else:
                time.sleep(3)
                player = TicTacToe.switchPlayers(player)
            if filledSpaces == 9 and TicTacToe.isThereWinner(player)==False:
                print("Game over! It's a tie!")

            
if True:
    while True:
        intro()
        play()
        print("Would you like to play again?(yes or no)")
        answer = input()
        while True:
            if answer=='yes':
              intro()
              play()
              print("Would you like to play again?(yes or no)")
              answer = input()
            else:
                break

        break
            
    
            
              
