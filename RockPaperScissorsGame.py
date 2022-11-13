import random

class Game:

    def get_choices(self):
        player_choice = input("Enter a choice (rock, paper or scissors): ")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}

        return choices

    def check_win(self, player, computer):
        print(f"You chose {player}, computer chose {computer}")
        if player == computer:
            return "It's a tie!"
            
        elif player == "rock": 
            if computer == "scissors":
                return "Rock smaskes scissors! You win!"
            else: 
                return "Paper covers rock! You lose."
        
        elif player == "paper": 
            if computer == "rock":
                return "Paper covers rock! You win!"
            else: 
                return "Scissors cut paper! You lose."
        
        elif player == "scissors": 
            if computer == "paper":
                return "Scissors cut paper! You win!"
            else: 
                return "Rock smaskes scissors! You lose."

    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number")

        while game_number < games_to_play:
            game_number += 1

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

            choices = self.get_choices()
            print(choices)
            result = self.check_win(choices["player"], choices["computer"])
            print(result)

        print("\nThanks for playing")

g = Game()
g.play()