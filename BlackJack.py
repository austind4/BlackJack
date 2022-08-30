import random

# List of card suites
suites = ["Clubs","Hearts","Diamonds","Spades"]

# List of card values
card_values= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Player Score
player_total = 0

# House Score
house_total = 0
class BlackJack():

    # Stores variables
    def __init__(self):
        self.suites = suites
        self.card_values = card_values
        self.player_total = player_total
        self.house_total = house_total

    def house_and_player_draw(self):
        # Randomly draws card and suite for player
        first_card = random.choice(self.card_values)
        player_card_drawn_identity = random.choice(self.suites)

        # Adds value to player_total
        self.player_total += first_card

        # Randomly draws card and suite for computer
        dealer_card = random.choice(self.card_values)
        house_card_drawn_identity = random.choice(self.suites)
        self.house_total += dealer_card

        # Shows player the current game state
        print(f'You have drawn {first_card} of {player_card_drawn_identity}')
        print(f'House has drawn {dealer_card} of {house_card_drawn_identity} and put a card in the hole')

        return

    def card_in_hole(self):
        # House Draws random card
        card_in_hole = random.choice(self.card_values)
        hole_card_suite = random.choice(self.suites)

        # Adds card in hole value to house total
        self.house_total += card_in_hole

        # Tells the player the House's current score
        print(f'The card in hole was {card_in_hole} of {hole_card_suite}. The house has a total of {self.house_total}')

        return

    def hit(self):

            # Draw another card
            new_card_number = random.choice(self.card_values)
            new_card_suite = random.choice(self.suites)
            self.player_total += new_card_number

            # Tells player their new total and what card they drew
            print(f'You drew a {new_card_number} of {new_card_suite} your new total is {self.player_total} ')

            return

    def house_hit(self):

            # Draw another card
            new_card_number = random.choice(self.card_values)
            new_card_suite = random.choice(self.suites)
            self.house_total += new_card_number

            # Tells player their new total and what card they drew
            print(f'House drew a {new_card_number} of {new_card_suite} the new total for the house is {self.house_total} ')

            # Automatically Lost
            return

    def score(self):
        # Method for scoring the game
        if self.player_total > self.house_total:
            print(f'You Won! with a total of {self.player_total} vs the house total of {self.house_total}')

        if self.player_total == self.house_total:
            print(f'Tie you both finished with a total of {self.player_total}')

        if self.player_total < self.house_total:
            print(f'You Lost the house finished with a total of {self.house_total}')

        return
    # Method for playing the game
    def play(self):

        # Confirms player wants to play game
        player = input("Play BlackJack? (Yes or No) ").lower()
        if player == "yes":
            game.house_and_player_draw()
        elif player == "no":
            print("Come again later!")
            return
        # Asks player if they want to hit or stand
        player = input("Hit or stand? ").lower()
        if player == "hit":
            game.hit()
            # Automatic loss condition
            if self.player_total > 21:
                print(f'Bust! you lost because {self.player_total} was over 21')
                return
        elif player == "stand":
            pass

        # House reveals card in the hole
        game.card_in_hole()
        if self.house_total <= 16:
            game.house_hit()

        if self.house_total > 21:
            print(f' You Won! The house went over 21 at with a total score of {self.house_total}')
            return
        # Asks player if they want to hit or stand
        player = input("Hit or stand? ").lower()
        if player == "hit":
            game.hit()
            # Automatic loss condition
            if self.player_total > 21:
                print(f'Bust! you lost because {self.player_total} was over 21')
                return
        elif player == "stand":
            pass

        game.score()

# Sets variable to the BlackJack class
game = BlackJack()
# Runs method through defined variable
game.play()

