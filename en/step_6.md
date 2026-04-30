<h2 class="c-project-heading--task">Split everyone into teams</h2>

Keep choosing players until everyone is in a team.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Keep the team name code from the last step, but replace the code that picks just one player for each team with a `while` loop. The loop should keep picking players until `players` is empty. For now, keep an **even number** of names in `players`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 13-20
---
from random import choice

players = ['Aisha', 'Kai', 'Linh', 'Mateo', 'Noor', 'Zuri']

team_names = ['Lightning Llamas', 'Pixel Penguins', 'Turbo Tigers', 'Dancing Dragons']
team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)

team_A = []
team_B = []

while len(players) > 0:
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

<div class="c-project-callout c-project-callout--tip">
Tip

Inside a <strong>while</strong> loop, indent the lines you want to repeat (4 spaces) so Python knows they belong to the loop.

</div>

## Now run your code

Run the program. Every player should appear in **exactly one** of the teams.

<div class="c-project-callout c-project-callout--debug" style="font-size: 1.1em">
Debug

If you see an `IndexError`, it usually means you have an odd number of players. In the next step, you will fix that.

</div>
