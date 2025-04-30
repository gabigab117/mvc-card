from models import SUITS, RANKS, Card, Deck, Player
from view import View


class Controller:
    def __init__(self, deck, view: View):
        self.players = list()
        self.deck = deck
        self.view = view
    
    def get_players(self):
        while len(self.players) < 5:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)
    
    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)
    
    def evaluate_game(self):
        last_player = self.players[0]
        best_candidate = self.players[0]
        
        for player in self.players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]
            
            if player_card > last_player_card:
                best_candidate = player
            last_player = player
        return best_candidate.name
    
    def rebuild_deck(self):
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
            self.deck.shuffle()
    
    def run(self):
        self.get_players()
        
        running = True
        while running:
            self.start_game()
            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)
            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True
            self.view.show_player_hand(player.name, player.hand)
            self.view.show_winner(self.evaluate_game())
            
            running = self.view.prompt_for_new_game()
            self.rebuild_deck()
