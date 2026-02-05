from random import choice

#create a list of players from a file
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

#create a list of team names from a file
team_names = []
file = open('team_names.txt', 'r')
team_names = file.read().splitlines()

#create empty team lists
team_A = []
team_B = []

#loop until there are no players left
while len(players) > 0:
  
    #choose a random player for team A
    player_A = choice(players)
    team_A.append(player_A)
    #remove the player from the players list
    players.remove(player_A)
  
    #break out of the loop if there are no players left
    if players == []: 
        break
  
    #choose a random player for team B
    player_B = choice(players)
    team_B.append(player_B)
    #remove the player from the players list
    players.remove(player_B)

#choose random team names for the 2 teams
team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)
team_names.remove(team_name_B)

#print the teams
print('\nHere are your teams:\n')
print(team_name_A, team_A)
print(team_name_B, team_B)