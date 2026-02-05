## Choosing lots of players

Next you'll need to make sure that every player has been chosen for a team.

--- task ---

Highlight your code for choosing players for team A and team B and press the tab key to indent the code.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 10-20
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

team_A = []
team_B = []


    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('Players left: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)

--- /code ---

--- /task ---

--- task ---

Add a __while__ loop to keep choosing players until the length of the `players` list is 0.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 9
---
while len(players) > 0:
    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('Players left: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)

--- /code ---

--- /task ---

--- task ---

Run your code to test it. You should see players being chosen for team A and team B until there are no more players left.

```
['Harry', 'Hermione', 'Neville', 'Ginny']
Hermione
Players left:  ['Harry', 'Neville', 'Ginny']
Harry
Players left:  ['Neville', 'Ginny']
Ginny
Players left:  ['Neville']
Neville
Players left:  []
```

--- /task ---

--- task ---

Add code to print your `team_A` list __after__ your `while` loop (making sure it is not indented).

This means that `team_A` will only be printed once, after all the players have been chosen.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 22
---
while len(players) > 0:
    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('Players left: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)

print('Team A', team_A)

--- /code ---

--- /task ---

--- task ---

You can do the same for `team_B`, and you can also delete the other print commands, as they were only there to test your code.

Here's how your code should look:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']

team_A = []
team_B = []

while len(players) > 0:
    player_A = choice(players)
    team_A.append(player_A)
    players.remove(player_A)
    
    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)

print('Team A', team_A)
print('Team B', team_B)

--- /code ---

--- /task ---

--- task ---

Test your code again and you should just see your list of players as well as your final teams.

```
Team A ['Hermione', 'Harry']
Team B ['Neville', 'Ginny']
```
--- /task ---






