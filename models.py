from collections import UserList
import random


SUITS = ("diamonds", "coeurs", "piques", "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False # visible ou cachée
        # Valeur du rang et de la suite selon l'index
        # Utile pour les comparaisons
        self._rank_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)
    
    def __str__(self):
        return f"{self.rank} de {self.suit}"
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other: "Card"):
        """
        Compare si cette carte est inférieure à une autre carte.
        La comparaison est d'abord basée sur le rang, puis sur la suite si les rangs sont égaux.
        2 de Coeur est inférieur à 3 de Trèfle.
        Si les rangs sont égaux, les suites sont comparées.
        Args:
            other (Card): L'autre carte à comparer
        Returns:
            bool: True si cette carte est inférieure à l'autre carte, False sinon
        Example:
            >>> card1 = Card('2', 'Coeur')
            >>> card2 = Card('3', 'Trèfle') 
            >>> card1 < card2
            True
        """
        
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score
        
        return self._suit_score < other._suit_score


card1 = Card("diamonds", "cinq")
card2 = Card("coeurs", "cinq")
print(card2 > card1) # True, car coeur a un index plus élevé


class Deck(UserList):
    def __init__(self):
        super().__init__()
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.append(card)
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self)
    
    def draw_card(self):
        """
        Ne fait rien de plus qu'un pop, mais plus lisible comme nom
        """
        try:
            return self.pop()
        except IndexError:
            return None


class Hand(UserList):
    def append(self, object):
        if not isinstance(object, Card):
            raise ValueError("Vous ne pouvez ajouter que des cartes")
        return super().append(object)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
