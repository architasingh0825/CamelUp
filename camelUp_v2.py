from colorama import Back, Style
import numpy as np
import copy
from itertools import product
import itertools


class Player:
    def __init__(self):
        self.bettingCards = {}
        self.money = 0

    def giveCard(self, color, betValue):
        ''' Adds selected card to dictionary of player cards '''
        if color not in self.bettingCards : self.bettingCards[color] = [betValue]
        else: self.bettingCards[color] += [betValue]

    def getCards(self):
        ''' Getter method to return cards a player has '''
        return self.bettingCards
    
    def payment(self, amount):
        self.money += amount

    def getMoney(self):
        return self.money

    
class GameBoard:

    def __init__(self, positions = None):

        ''' Code to initalize game board. We roll the dice and randomly place camels along spots. '''

        self.remainingDice = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
        if positions == None:
            self.positions = {0:[]}
            for i in self.remainingDice:
                rolls = [1,2,3]
                startSpot = int(np.random.choice(rolls))
                if startSpot in self.positions:
                    self.positions[startSpot].append(i)
                else:
                    self.positions[startSpot] = [i]
        else:
            self.positions = positions
        self.diceTents = {}
    
    def printDiceTents(self):
        return self.diceTents
    
    def isEmptyDice(self):
        return len(self.remainingDice) == 0
    
    def getPositions(self, positions):
        if positions == None: positions = self.positions # CHANGED
        positions = {k: positions[k] for k in sorted(positions)}
        return positions
    

    def rollDice(self, player: Player, spotsToMove = None, colorRolled = None):

        ''' Code to simulate a roll. Removes the color from the dice list so one color isn't rolled twice '''
        rolls = [1,2,3]
        
        if spotsToMove == None and colorRolled == None:
            spotsToMove = np.random.choice(rolls)
            colorRolled = np.random.choice(self.remainingDice)
            self.moveCamel(colorRolled, spotsToMove, None)
            self.remainingDice.remove(colorRolled)
            player.payment(1)
            self.diceTents[colorRolled] = spotsToMove
        else:
            self.moveCamel(colorRolled, spotsToMove, None)



    def moveCamel(self, color, spotsToMove, positions):

        ''' Code to move camel spotsToMove positions from current position. Does not currently account for camel being on top of another '''
        #posCopy = {k: v for k, v in self.positions.items()}
        if positions == None: positions = self.positions # CHANGED
        posCopy = copy.deepcopy(self.positions)
        for i in posCopy:
            ''' Checks if camel is alone on position '''

            if color in positions[i]:
                camelList = positions[i]
                colorIndex = positions[i].index(color)
                camelList = camelList[colorIndex:]
                # self.positions[i] = [i for i in self.positions[i] if i not]
                positions[i] = positions[i][:colorIndex]
                # self.positions[i].remove([])
                newPosition = int(i + spotsToMove)
                if newPosition in positions:
                    positions[newPosition] += camelList
                else:
                    positions[newPosition] = camelList

    def replace_char_at_index(self, original_string, index, new_char):
        new_string = original_string[:index] + new_char + original_string[index + 1:]
        return new_string

    def getColors(self, color):

        if color == 'R':
            return Back.RED + "R" + Style.RESET_ALL
        if color == 'B':
            return Back.BLUE + "B" + Style.RESET_ALL
        if color == 'Y':
            return Back.YELLOW + "Y" + Style.RESET_ALL
        if color == 'G':
            return Back.GREEN + "G" + Style.RESET_ALL
        if color == 'P':
            return Back.MAGENTA + "P" + Style.RESET_ALL

    def printBoard(self):
        line1 = "🌴" + " "*53 + "|🏁"
        line2 = "🌴" + " "*53 + "|🏁"
        line3 = "🌴" + " "*53 + "|🏁"
        line4 = "🌴" + " "*53 + "|🏁"
        line5 = "🌴" + " "*53 + "|🏁"

        for position in self.positions:
            camelsAtPos = self.positions[position]
            if len(camelsAtPos) == 5: 
                line1 = self.replace_char_at_index(line1, 1+(position-1)*3, self.positions[position][0][0])
                line2 = self.replace_char_at_index(line2, 1+(position-1)*3, self.positions[position][1][0])
                line3 = self.replace_char_at_index(line3, 1+(position-1)*3, self.positions[position][2][0])
                line4 = self.replace_char_at_index(line4, 1+(position-1)*3, self.positions[position][3][0])
                line5 = self.replace_char_at_index(line5, 1+(position-1)*3, self.positions[position][4][0])
            if len(camelsAtPos) == 4:
                line1 = self.replace_char_at_index(line1, 1+(position-1)*3, self.positions[position][0][0])
                line2 = self.replace_char_at_index(line2, 1+(position-1)*3, self.positions[position][1][0])
                line3 = self.replace_char_at_index(line3, 1+(position-1)*3, self.positions[position][2][0])
                line4 = self.replace_char_at_index(line4, 1+(position-1)*3, self.positions[position][3][0])
            if len(camelsAtPos) == 3:
                line1 = self.replace_char_at_index(line1, 1+(position-1)*3, self.positions[position][0][0])
                line2 = self.replace_char_at_index(line2, 1+(position-1)*3, self.positions[position][1][0])
                line3 = self.replace_char_at_index(line3, 1+(position-1)*3, self.positions[position][2][0])
            if len(camelsAtPos) == 2:  
                line1 = self.replace_char_at_index(line1, 1+(position-1)*3, self.positions[position][0][0])
                line2 = self.replace_char_at_index(line2, 1+(position-1)*3, self.positions[position][1][0])
            if len(camelsAtPos) == 1:
                line1 = self.replace_char_at_index(line1, 1+(position-1)*3, self.positions[position][0][0])

        print(line5)
        print(line4)
        print(line3)
        print(line2)
        print(line1)
        
        print("  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16")



class BettingCards:
    def __init__(self):
        ''' Initializes all betting cards as available '''
        self.bettingCards = {'R': [5, 3, 2, 2], 'B': [5, 3, 2, 2], 'G': [5, 3, 2, 2], 'Y': [5, 3, 2, 2], 'P': [5, 3, 2, 2]}

    def printTicketTents(self):
        printOuts = []
        for color in self.bettingCards:
            if len(self.bettingCards[color]) == 0:
                printOuts.append("X")
            else:
                printOuts.append(self.bettingCards[color][0])
        return printOuts

    def assignCard(self, color, player: Player):

        ''' Assigns card to given player '''
        if color not in self.bettingCards: return False
        if len(self.bettingCards[color]) > 0: betValue = self.bettingCards[color][0]
        else: betValue = -1
        if self.isAvailable(color, betValue, None):

            player.giveCard(color, betValue)
            self.bettingCards[color].remove(betValue)
            return True
        else:
            if(color in self.bettingCards):
                print("Betting card has already been selected.")
            else:
                print("Not a valid color selection.")
            
            return False

    def isAvailable(self, color, betValue, bettingCards): # CHANGED THIS

        ''' Checks if card is available '''
        if bettingCards == None: bettingCards = self.bettingCards
        return betValue in bettingCards[color]

class Leaderboard:
    def __init__(self):
        ""
    
    def getTopTwo(self, board: GameBoard, positions: GameBoard):
        ''' Returns top two camels at conclusion of round. '''
        if positions == None: positions = board.getPositions(None)  # CHANGED
        topTwo = {1: [], 2: []}
        temp = []
        for i in positions:
            currentCamels = positions[i]
            temp.append(currentCamels)
        topTwo[1] = temp[-1]
        topTwo[2] = temp[-2]
        return topTwo

            
class PlayGame:
    def __init__(self):
        ""
    
    def payOut(self, game: GameBoard, leaderboard: Leaderboard, players: list[Player]):
        ''' Pays out to every camel '''
        topTwo = leaderboard.getTopTwo(game, None) # CHANGED
        for player in players:
            cards = player.getCards()
            for card in cards:
                if card in topTwo[1]:
                    player.payment(sum([x for x in cards[card]]))
                elif card in topTwo[2]:
                    player.payment(sum([1 for x in cards[card]]))
                else:
                    player.payment(sum([-1 for x in cards[card]]))

class EV:
    def __init__(self): 
        self.probabilities = {"R":[0, 0], "G":[0, 0], "B":[0, 0], "Y":[0, 0], "P":[0, 0]}

    def makeOrders(self, game: GameBoard, players: list[Player], leaderboard: Leaderboard, bettingCards: BettingCards):
        dice = game.remainingDice
        positions = []
        for i in range(len(dice)):
            positions.append(i)
        permutation = list(product(dice, positions))

        rolls = [1, 2, 3]
        dice_count = len(game.remainingDice)

        # dice rolls
        temp = [list(sequence) for sequence in product(rolls, repeat=dice_count)]

        # list of tuples
        permutations = list(itertools.permutations(dice)) # dice order

        for permutation in permutations:
            for roll in temp:
                self.results(permutation, roll, game.getPositions(None), players[0], leaderboard) # player doesn't matter
        self.makePercentages(self.factorial(dice_count) * 3 ** dice_count)
        print(self.probabilities)
        for card in bettingCards.bettingCards:
            for amt in bettingCards.bettingCards[card]:
                cardEV = self.getEV(card, amt)
                print(card, amt, cardEV)

    def results(self, permutation: tuple, order: list, positions: dict, player: Player, leaderboard: Leaderboard):
        ''' Who wins and who gets second place '''
        board = GameBoard(copy.deepcopy(positions))
        for i in range(len(permutation)):
            dice = permutation[i]
            steps = order[i]
            board.rollDice(player=player,spotsToMove=steps,colorRolled=dice)
        winners = leaderboard.getTopTwo(board, None) # None
        first = winners[1]
        second = winners[2]
        self.probabilities[first[0][0]][0] += 1
        self.probabilities[second[0][0]][1] += 1
    
    def makePercentages(self, total: int):
        for color in self.probabilities:
            self.probabilities[color][0] = round(self.probabilities[color][0] / total, 2)
            self.probabilities[color][1] = round(self.probabilities[color][1] / total, 2)
    
    def factorial(self, n):
        count = 1
        while n > 0:
            count *= n
            n -= 1
        return count

    def getEV(self, cardColor: str, cardAmt: int):
        probFirst = self.probabilities[cardColor][0]
        probSecond = self.probabilities[cardColor][1]
        result = probFirst * cardAmt + probSecond * 1 + (1 - probFirst - probSecond) * -1
        return round(result, 2)


if __name__ == "__main__":
    game = PlayGame()
    player1 = Player()
    player2 = Player()
    board = GameBoard()
    playGame = PlayGame()
    bettingCards = BettingCards()
    
    leaderBoard = Leaderboard()
    print((" 🐪 🏜️ "*12).lstrip())
    print(" " * 24 + "WELCOME TO CAMEL UP!!!" + " "*24)
    print((" 🐪 🏜️ "*12).lstrip())
    isPlayer1Turn = True
    board.printBoard()
    while not board.isEmptyDice():
        print("Ticket tents: ", end="")
        ticketTents = bettingCards.printTicketTents()
        print(Back.RED + str(ticketTents[0]) + Style.RESET_ALL + " " + 
            Back.BLUE + str(ticketTents[1]) + Style.RESET_ALL + " " +
            Back.GREEN + str(ticketTents[2]) + Style.RESET_ALL + " " +
            Back.YELLOW + str(ticketTents[3]) + Style.RESET_ALL + " " +
            Back.MAGENTA + str(ticketTents[4]) + Style.RESET_ALL, end="")
        
        print(" " * 26, "Dice tents: ", end="")

        diceTents = board.printDiceTents()

        toPrintOutDice = ""

        count = 0
        for dice in diceTents:
            if dice == "Red":
                toPrintOutDice += Back.RED + str(diceTents[dice]) + Style.RESET_ALL + " "
            elif dice == "Green":
                toPrintOutDice += Back.GREEN + str(diceTents[dice]) + Style.RESET_ALL + " "
            elif dice == "Blue":
                toPrintOutDice += Back.BLUE + str(diceTents[dice]) + Style.RESET_ALL + " "
            elif dice == "Yellow":
                toPrintOutDice += Back.YELLOW + str(diceTents[dice]) + Style.RESET_ALL + " "
            elif dice == "Purple":
                toPrintOutDice += Back.MAGENTA + str(diceTents[dice]) + Style.RESET_ALL + " "
            count += 1
        while count < 5:
            count += 1
            toPrintOutDice += Back.WHITE + " " + Style.RESET_ALL + " "

        print(toPrintOutDice)
        if isPlayer1Turn: 
            currentPlayer = player1
            print("Player 1 Turn- ", end="")
        else: 
            currentPlayer = player2
            print("Player 2 Turn- ", end = "")

        move = input("(B)et or (R)oll? ")
        while(move.upper() != "B" and move.upper() != "R"):
            print("Try again! Only input a move B or R.")
            move = input("(B)et or (R)oll? ")
        if move.lower() == "b":
            Ev = EV()
            Ev.makeOrders(board, [player1, player2], leaderBoard, bettingCards)
            color = input("Color (R, B, G, Y, P) ").upper()
            isAvail = bettingCards.assignCard(color, currentPlayer)
            while not isAvail:
                print("Try Again")
                move = input("(B)et or (R)oll? ")
                while(move.upper() != "B" and move.upper() != "R"):
                    print("Try again! Only input a move B or R.")
                    move = input("(B)et or (R)oll? ")
                if move.lower() == "b":
                    color = input("Color (R, B, G, Y, P) ").upper()
                    isAvail = bettingCards.assignCard(color, currentPlayer)
                elif move.lower() == 'r':
                    board.rollDice(currentPlayer)
                    print(board.getPositions(None)) 

            # bettingCards.assignCard(color, betValue, currentPlayer)

        elif move.lower() == "r": 
            board.rollDice(currentPlayer)
            board.printBoard()


        else: 
            print("REDOOOOOO")
        
        left_alignment = "Player 1 has " + str(player1.getMoney()) + " coin(s). Bets: " +  str(player1.getCards())
        right_alignment = " Player 2 has " + str(player2.getMoney()) + " coin(s). Bets: " + str(player2.getCards())
        total_width = 40  # Example width; adjust based on your needs

        print(left_alignment, " " * 15, right_alignment)


        isPlayer1Turn = not(isPlayer1Turn)
    topTwo = leaderBoard.getTopTwo(board, None) # CHANGED
    print("".join(topTwo[1]), "comes in first!! 🥇🥇🥇",)
    print("".join(topTwo[2]), "comes in second!! 🥈🥈🥈")
    playGame.payOut(board, leaderBoard, [player1, player2])
    print("Player 1 ended the leg with", player1.getMoney(), "coins.")
    print("Player 2 ended the leg with", player2.getMoney(), "coins.")
    print((" 🐪 🏜️ "*12).lstrip())
    print(" "*25, "Thanks for playing!", " "*25)
    print((" 🐪 🏜️ "*12).lstrip())



