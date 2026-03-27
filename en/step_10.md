<h2 class="c-project-heading--task">Load team names from a file</h2>

--- task ---
After loading players from a file, store team names in `team_names.txt` and load them into your program.
--- /task ---

--- task ---
Create a file called `team_names.txt` and put one team name on each line. Use the same names that were in your `team_names` list.

--- /task ---

--- task ---
Keep the rest of your program the same. Replace the `team_names` list with code that reads `team_names.txt` into a list.

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

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
file.close()

team_names = []  # make a list called team_names
file = open('team_names.txt', 'r')  #  Open the team_names.txt file
team_names = file.read().splitlines()   # add lines from file into the list
file.close()

team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)

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
Edit `team_names.txt` and run again. Your new names should appear in the output.
--- /task ---
