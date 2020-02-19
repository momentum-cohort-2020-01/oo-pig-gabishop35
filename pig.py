import random


class Game:
    def __init__(self):
        self.player = Player()
        self.opponent = Opponent()
        self.die = Die()

    def select_who_starts():
        


    #randomly select which player goes first

    def turn(self):
        
        choice = input("Do you want to (r)oll or (h)old?")
        if choice == "r":
                #roll again
            if choice == "h":
                    #end turn, add points to total


    #game ends when player reaches 100




    pass

class Die:
    def __init__(self):

    def roll_die_once(self):
    roll = random.randint(1,6)        
    print(roll)
    return roll




    #value of 1 ends turn and clears all points from turn
    pass

class Player:
    def __init__(self, name):
        self.name = name
        self.turn_score = []
        self.score = 0

    def __str__(self):
        return f'{self.name}'
    #player rolls
    #player holds



    def sum_turn_score(self):
        sum = sum(roll)

    def show_turn_score(self):
        print("Your score on this turn is ", [f'{sum_turn_score}'])

    def show_score(self):
        print("Your total score is ", [f'{sum_score}'])

    pass

class Opponent:
    def __init__(self, name):
        self.name = name
        self.turn_score = []
        self.score = 0

    def __str__(self):
    return f'{self.name}'
    