<h2 class="c-project-heading--task">Add random team names</h2>

--- task ---
Give each team a random team name.
--- /task ---

--- task ---
Create a `team_names` list and choose a different random name for each team.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8-12,29-33
---
from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
file.close()

team_names = ['Alligators', 'Gorillas', 'Eagles', 'Pythons']  # names to choose from
team_name_A = choice(team_names)  # pick a name for Team A
team_names.remove(team_name_A)  # remove it so Team B can't use it
team_name_B = choice(team_names)  # pick a different name for Team B

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

print(team_name_A, team_A)
print(team_name_B, team_B)
--- /code ---
</div>
--- /task ---

--- task ---
### Test
Run your program a few times. The team names should change, and **Team A and Team B should never get the same name**.
--- /task ---
