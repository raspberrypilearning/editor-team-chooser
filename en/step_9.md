<h2 class="c-project-heading--task">Load players from a file</h2>

--- task ---
Read player names from `players.txt` instead of writing them inside your code.
--- /task ---

--- task ---
Create a file called `players.txt` and put one player name on each line. Use the same names that were in your `players` list.

--- /task ---


--- task ---
Keep the rest of your program the same. Replace the `players` list with code that reads names from the file using `splitlines()`:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8-11
---
from random import choice

team_names = ['Lightning Llamas', 'Pixel Penguins', 'Turbo Tigers', 'Dancing Dragons']
team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
file.close()

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
Run the program. If you change the names in `players.txt`, your teams should change too.
--- /task ---
