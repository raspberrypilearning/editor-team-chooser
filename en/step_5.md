<h2 class="c-project-heading--task">Create two teams</h2>

--- task ---
Create two empty teams and put one random player into each team.
--- /task ---

--- task ---
Create `team_A` and `team_B`, then choose a player for each team and remove them from `players`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5-16
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny', 'Luna', 'Ron']

team_A = []  # Team A players go here
team_B = []  # Team B players go here

player_A = choice(players)
team_A.append(player_A)
players.remove(player_A)

player_B = choice(players)
team_B.append(player_B)
players.remove(player_B)

print('Team A:', team_A)
print('Team B:', team_B)
print('Players left:', players)
--- /code ---
</div>
--- /task ---

--- task ---
### Test
Run the program. You should see **one player in each team**, and fewer players left in the `players` list.
--- /task ---
