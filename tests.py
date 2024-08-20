import unittest
from camelUp import Player, BettingCards, Leaderboard, GameBoard

class Test(unittest.TestCase):
    def setUp(self):
        ''' This runs before each test '''
        self.remainingDice = ['Red', 'Blue', 'Green']

        self.positions = {
            0: [],
            1: ['Red', 'Blue', 'Green'],
            2: ['Yellow'],
            3: ['Purple']
        }

        self.bettingCards = {'R': [3, 2, 2], 'B': [5, 3, 2, 2], 'G': [3, 2, 2], 'Y': [3, 2, 2], 'P': [5, 3, 2, 2]}
        
        self.player1 = Player()
        self.card = BettingCards()
        self.leader = Leaderboard()
        self.board = GameBoard()

    def test_0(self):
        ''' tests if input color is invalid'''
        actual = self.card.assignCard("Black", self.player1) 
        self.assertFalse(actual) 

    def test_1(self): 
        '''tests if card is available'''
        bettingCards = {'R': [3, 2, 2], 'B': [5, 3, 2, 2], 'G': [3, 2, 2], 'Y': [3, 2, 2], 'P': [5, 3, 2, 2]}
        actual = self.card.isAvailable('R', 5, bettingCards)
        self.assertFalse(actual)
        
    def test_2(self):
        '''tests if card is available'''
        bettingCards = {'R': [3, 2, 2], 'B': [5, 3, 2, 2], 'G': [3, 2, 2], 'Y': [3, 2, 2], 'P': [5, 3, 2, 2]}
        actual = self.card.isAvailable('R', 2, bettingCards)
        self.assertTrue(actual)

    def test_3(self):
        '''tests if getTopTwo works'''
        positions = {
            0: [],
            1: ['Red', 'Blue', 'Green'],
            2: ['Yellow'],
            3: ['Purple']
        }
        actual = self.leader.getTopTwo(self.board, positions)
        
        expected = {1: ['Purple'], 2: ['Yellow']}
        self.assertEqual(actual, expected)

    def test_4(self): 
        '''tests if camels moved correctly'''
        positions = {
            0: [],
            1: ['Red', 'Blue', 'Green'],
            2: ['Yellow'],
            3: ['Purple']
        }
        self.board.moveCamel("Red", 2, positions)
        actual = self.board.getPositions(positions)
        expected = {
            0: [],
            1: [],
            2: ['Yellow'],
            3: ['Purple', 'Red', 'Blue', 'Green']
        }
        self.assertEqual(actual, expected)

    def test_5(self):
        '''woooooooooo'''

if __name__ == "__main__":
    unittest.main()
