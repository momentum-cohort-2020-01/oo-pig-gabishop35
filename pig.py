import random


class Game:
    def __init__(self):
        self.player = Player("Player 1")
        self.opponent = Opponent("Opponent")
        self.die = Die()

    def select_who_starts(self):
        first = random.randint(0, 1)
        if first == 0:
            print("Opponent goes first!")
            self.opponent_turn()
        else:
            print("Player 1 goes first!")
            self.player_turn()

    # randomly select which player goes first

    def player_turn(self):
        self.player.show_turn_score = 0
        print("Player 1's turn!")
        choice = "r"
        while choice == "r":
            self.player.turn_score += self.die.roll()
            choice = input("Do you want to (r)oll or (h)old?")
            print(choice)
        self.player.score += self.player.turn_score
        self.opponent_turn()


    def opponent_turn(self):
        self.opponent.turn_score = 0
        print("Opponent's turn!")
        while self.opponent.turn_score < 20:
            self.opponent.turn_score += self.die.roll()

        self.opponent.score += self.opponent.turn_score
        self.player_turn()
            # end turn, add points to total
            # game ends when player reaches 100



class Die:

    def roll(self):
        roll = random.randint(1, 6)
        print(roll)
        return roll

    # value of 1 ends turn and clears all points from turn



class Player:
    def __init__(self, name):
        self.name = name
        self.turn_score = 0
        self.score = 0

    def __str__(self):
        return f'{self.name}'
    # player rolls
    # player holds

    

    def show_turn_score(self):
        print("Your score on this turn is ", f'{self.turn_score}')

    def show_score(self):
        print("Your total score is ", f'{self.score}')




class Opponent:
    def __init__(self, name):
        self.name = name
        self.turn_score = 0
        self.score = 0

    def __str__(self):
        return f'{self.name}'

    # def turn(self):
    #     choice = input("Do you want to (r)oll or (h)old?")
    #     if choice == "r":
    #         self.roll(self.opponent)
    #     # if choice == "h":


game = Game()
game.select_who_starts()
