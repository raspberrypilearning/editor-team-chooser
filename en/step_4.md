## Random players

Let's choose random players!

--- task ---

To be able to get a random player from your `players` list, first you'll need to import the `choice` part of the `random` module.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

print(players[0])
print(players[1])

--- /code ---

--- /task ---

--- task ---

To get a random player, you can use `choice`. (You can also delete the code to print individual players.)

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

print(choice(players))

--- /code ---

--- /task ---

--- task ---

Test your `choice` code a few times and you should see a different player being chosen each time.

--- /task ---

--- task ---

You can also create a new variable called `playerA`, and use it to store your random player.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

player_A = choice(players)
print(player_A)

--- /code ---

--- /task ---

--- task ---

You'll need a new list to store all of the players in team A. To start with, this list should be empty.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

team_A = []

player_A = choice(players)
print(player_A)

--- /code ---

--- /task ---

--- task ---

You can now add your randomly chosen player to `teamA`. To do this, you can use `teamA.append` (__append__ means add to the end).

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 10
---
player_A = choice(players)
print(player_A)
team_A.append(player_A)

--- /code ---

--- /task ---

--- task ---

Now that your player has been chosen, you can remove them from your list of `players`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 11
---
player_A = choice(players)
print(player_A)
team_A.append(player_A)
players.remove(player_A)

--- /code ---

--- /task ---

--- task ---

Test this code by adding a `print` command, to show the `players` left to choose from.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 12
---
player_A = choice(players)
print(player_A)
team_A.append(player_A)
players.remove(player_A)
print('Players left: ', players)

--- /code ---

--- /task ---




