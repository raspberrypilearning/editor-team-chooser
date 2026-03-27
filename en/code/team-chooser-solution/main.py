from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
file.close()

team_names = []
file = open('team_names.txt', 'r')
team_names = file.read().splitlines()
file.close()

team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)

team_A = []
team_B = []

while len(players) > 0:
    player_A = choice(players)
    team_A.append(player_A)
    players.remove(player_A)

    if players == []:
        break

    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)

print('\nHere are your teams:\n')
print(team_name_A, team_A)
print(team_name_B, team_B)
