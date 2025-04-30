from controller import Controller
from models import Deck
from view import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()


main()
