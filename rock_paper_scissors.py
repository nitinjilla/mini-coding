import random
import operator

def RockPaperScissors(human_name, human_choice):
        computer_options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_options)
        print(computer_choice)
        if human_choice in computer_options:
                if computer_options.index(human_choice) == computer_options.index(computer_choice):
                        print(f'Game {counter}: Tie!\n')
                        return 0

                if (computer_options.index(human_choice) == 2) and (computer_options.index(computer_choice) == 0):
                        players['Computer'] += 1
                        print(f'Game {counter}: Computer won.\n')
                        return 0

                if (computer_options.index(human_choice) == 0) and (computer_options.index(computer_choice) == 2):
                        players[human_name] += 1
                        print(f'Game {counter}: {human_name} won.\n')
                        return 0
                
                if (computer_options.index(human_choice) > computer_options.index(computer_choice)):
                        players[human_name] += 1
                        print(f'Game {counter}: {human_name} won.\n')
                else:
                        players['Computer'] += 1
                        print(f'Game {counter}: Computer won.\n')
                        
        else:
                print('Enter a valid option')

counter = 1
human_name = input('Enter your name \n')
players = {human_name: 0, 'Computer': 0}
while counter <= 5:
        human_choice = input('\nThrow a rock, paper or scissors \n').lower()
        RockPaperScissors(human_name, human_choice)
        counter += 1

winner = max(players.items(), key =  operator.itemgetter(1))[0]
loser = min(players.items(), key =  operator.itemgetter(1))[0]

if players[human_name] == players['Computer']:
        print("It's a draw! \n\n{} {} - {} Computer".format(human_name, players[human_name], players['Computer']))
else:
        print("{} won this round. \n\n{} {} - {} Computer".format(winner, human_name, players[human_name], players['Computer']))

