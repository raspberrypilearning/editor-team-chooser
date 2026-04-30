<h2 class="c-project-heading--task">Add random team names</h2>

Now that each team has one player, give each team a fun random name.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Keep your code from the last step. Add a `team_names` list, choose a different name for each team, and print the team names instead of `Team A` and `Team B`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8-11,21-22
---
from random import choice

players = ['Aisha', 'Kai', 'Linh', 'Mateo', 'Noor', 'Zuri']

team_A = []
team_B = []

team_names = ['Lightning Llamas', 'Pixel Penguins', 'Turbo Tigers', 'Dancing Dragons']
team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)

player_A = choice(players)
team_A.append(player_A)
players.remove(player_A)

player_B = choice(players)
team_B.append(player_B)
players.remove(player_B)

print(team_name_A, team_A)
print(team_name_B, team_B)
--- /code ---
</div>

## Now run your code

Run your program a few times. The team names should change, and the two teams should not get the same name.
