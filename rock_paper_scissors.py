# If rock, paper and scissor are kept in the spoken order, then it can be seen that the one with higher index wins. However, that is 
# not the case for rock-scissors pair. Two 'if' statements are used to solve this anomaly. 
# The player with the highest score at the end of best of five game is the winner.

import random, operator

def RockPaperScissors(human_choice):
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        print(computer_choice)
        if human_choice in options:
                if options.index(human_choice) == options.index(computer_choice):
                        print(f'Game {counter}: Tie!\n')
                        return 0

                if (options.index(human_choice) == 2) and (options.index(computer_choice) == 0):
                        players['Computer'] += 1
                        print(f'Game {counter}: Computer won.\n')
                        return 0

                if (options.index(human_choice) == 0) and (options.index(computer_choice) == 2):
                        players[human_name] += 1
                        print(f'Game {counter}: {human_name} won.\n')
                        return 0
                
                if (options.index(human_choice) > options.index(computer_choice)):
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
        RockPaperScissors(human_choice)
        counter += 1

winner = max(players.items(), key =  operator.itemgetter(1))[0]

if players[human_name] == players['Computer']:
        print("It's a draw! \n\n{} {} - {} Computer".format(human_name, players[human_name], players['Computer']))
else:
        print("{} won this round. \n\n{} {} - {} Computer".format(winner, human_name, players[human_name], players['Computer']))

