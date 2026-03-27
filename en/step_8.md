<h2 class="c-project-heading--task">Handle an odd player</h2>

--- task ---
Make your program work even if there’s an odd number of players.
--- /task ---

--- task ---
Keep your `while` loop from the last step. Add one more name to `players` so there’s an odd number of players, then add a check after Team A gets a player so Team B only picks if there are players left.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 17-18
---
from random import choice

players = ['Aisha', 'Kai', 'Linh', 'Mateo', 'Noor', 'Zuri', 'Sofia']

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
    if players == []:  # stop if Team A just took the last player
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
Run the program with an odd number of players. One team should have **one extra player**, and the program should not crash.
--- /task ---
