#!/bin/python3

from random import choice

players = []
file = open('team-chooser-finished-players.txt', 'r')
players = file.read().splitlines()
file.close()

teamNames = []
file = open('team-chooser-finished-teamNames.txt', 'r')
teamNames = file.read().splitlines()
file.close()

teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)

teamA = []
teamB = []

while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)

  if players == []:
    break

  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)

print('\nHere are your teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)
