import random
import time

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            p_move = input("Rock, Paper, Scissors? > ").lower()
            valid_input = ["rock", "paper", "scissors"]
            if p_move not in valid_input:
                print("Please enter a valid input\n")
            else:
                return p_move


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = ""

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.their_move not in moves:
            self.my_move = random.choice(moves)
            return self.my_move
        else:
            self.my_move = self.their_move
            return self.my_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = ""

    def move(self):
        if self.my_move == "":
            self.my_move = random.choice(moves)
            return self.my_move
        else:
            if self.my_move == "rock":
                self.my_move = "paper"
                return self.my_move
            if self.my_move == "paper":
                self.my_move = "scissors"
                return self.my_move
            if self.my_move == "scissors":
                self.my_move = "rock"
                return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scorep1 = 0
        self.scorep2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")
        time.sleep(1)
        if move1 == move2:
            print("It's a tie!")
            print(f"Score: P1 - {self.scorep1}  P2 - {self.scorep2}\n")
            time.sleep(1)

        else:
            if beats(move1, move2):
                self.scorep1 += 1
                print("You win")
                print(f"Score: P1 - {self.scorep1}  P2 - {self.scorep2}\n")
                time.sleep(1)
            else:
                self.scorep2 += 1
                print("You lose")
                print(f"Score: P1 - {self.scorep1}  P2 - {self.scorep2}\n")
                time.sleep(1)

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        self.final_score()

    def final_score(self):
        if self.scorep1 > self.scorep2:
            print("Player 1 wins the game!")
            print(f"Score: P1 - {self.scorep1}  P2 - {self.scorep2}\n")
            time.sleep(1)

        if self.scorep2 > self.scorep1:
            print("Player 2 wins the game!")
            print(f"Score: P1 - {self.scorep1}  P2 - {self.scorep2}\n")
            time.sleep(1)

        if self.scorep1 == self.scorep2:
            print("It is a tie! There is no Winner")
            print(f"Score: P1 - {self.scorep1}  P2 - {self.scorep2}\n")
            time.sleep(1)

        play_again()


def play_again():
    retry = input("Would you like to play again? (Y/N)").lower()
    print("")
    if retry == "y":
        game.scorep1 = 0
        game.scorep2 = 0
        game.play_game()
    elif retry == "n":
        print("Thanks for playing")
    else:
        print("Please enter a valid input")
        play_again()


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player())
    game.play_game()
