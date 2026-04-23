<h2 class="c-project-heading--task">Create two teams</h2>

Create two empty teams and put one random player into each team.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Keep your `players` list and `choice` import, but replace the old `player` code with `team_A` and `team_B`. Then choose one player for each team and remove them from `players`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5-18
---
from random import choice

players = ['Aisha', 'Kai', 'Linh', 'Mateo', 'Noor', 'Zuri']

team_A = []  # Team A players go here
team_B = []  # Team B players go here

player_A = choice(players)  # choose a random player for Team A
team_A.append(player_A)     # add them to Team A
players.remove(player_A)    # remove them so they can't be picked again

player_B = choice(players)  # choose a random player for Team B
team_B.append(player_B)     # add them to Team B
players.remove(player_B)    # remove them so they can't be picked again

print('Team A:', team_A)    # show Team A
print('Team B:', team_B)    # show Team B
print('Players left:', players)  # show anyone not yet chosen
--- /code ---
</div>

## Now run your code

Run the program. You should see **one player in each team**, and fewer players left in the `players` list.
