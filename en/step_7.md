<h2 class="c-project-heading--task">Load players from a file</h2>

--- task ---
Read player names from `players.txt` instead of writing them inside your code.
--- /task ---

--- task ---
Create a file called `players.txt` and put one player name on each line. Make sure you have an **even number** of names!

--- /task ---


--- task ---
Update your code to read names from the file with `splitlines()`, by replacing the names list:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3-6
---
from random import choice

players = []  # make a list called players
file = open('players.txt', 'r')  #  Open the players.txt file
players = file.read().splitlines()   # add lines from file into the list
file.close()

team_A = []
team_B = []

while len(players) > 0:

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
Run the program. If you change the names in `players.txt`, your teams should change too.
--- /task ---
