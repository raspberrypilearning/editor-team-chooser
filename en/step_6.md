<h2 class="c-project-heading--task">Split everyone into teams</h2>

--- task ---
Keep choosing players until everyone is in a team.
--- /task ---

--- task ---
Use a `while` loop so the program keeps picking players until `players` is empty.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-26
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny', 'Luna', 'Ron']

team_A = []
team_B = []

while len(players) > 0:  # repeat until there are no players left

    player_A = choice(players)
    team_A.append(player_A)
    players.remove(player_A)

    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)

print('Team A:', team_A)
print('Team B:', team_B)
--- /code ---
</div>
--- /task ---

--- task ---
### Test
Run the program. Every player should appear in **exactly one** of the teams.
--- /task ---
