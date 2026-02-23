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
line_highlights: 7-16
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

<div class="c-project-callout c-project-callout--tip">
Tip

Inside a <strong>while</strong> loop, indent the lines you want to repeat (4 spaces) so Python knows they belong to the loop.

</div>

--- /task ---

--- task ---

### Test
Run the program. Every player should appear in **exactly one** of the teams.

<div class="c-project-callout c-project-callout--debug" style="font-size: 1.1em">
Debug

If you see this error:

`IndexError: list index out of range on line 14 of main.py`

It usually means your code is trying to get another player when the list is already empty. This can happen when you have an odd number of players, so Team A takes the last player and then Team B still tries to pick one more.

</div>

--- /task ---
