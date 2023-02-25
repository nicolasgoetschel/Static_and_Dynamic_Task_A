import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    card_1 = Card("Hearts", 1)
    card_2 = Card("Spades", 2)
    
    def test_check_for_ace_with_ace_card__true(self):
        result = CardGame.check_for_ace(self, self.card_1)
        self.assertEqual(True, result)

    def test_check_for_ace__false(self):
        result = CardGame.check_for_ace(self, self.card_2)
        self.assertEqual(False, result)

    def test_highest_card__(self):
        result = CardGame.highest_card(self, self.card_1, self.card_2)
        self.assertEqual(self.card_2, result)
    
    def test_cards_total(self):
        cards = [self.card_1, self.card_2]
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 3", result)