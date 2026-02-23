<h2 class="c-project-heading--task">Handle an odd player</h2>

--- task ---
Make your program work even if there’s an odd number of players.
--- /task ---

--- task ---
Add one more name to `players.txt` so there’s an odd number of players, then update your code to avoid picking for Team B when no players are left.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 16-18
---
from random import choice

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

    if players == []:  # stop if Team A just took the last player
        break

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
Run the program with an odd number of players. One team should have **one extra player**, and the program should not crash.
--- /task ---
