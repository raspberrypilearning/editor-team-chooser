## Players

Let's start by creating a list of players to choose from.

--- task ---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

--- /task ---

--- task ---

You can use a variable to store a __list__ of players. 

The list should be in square brackets `[ ]`, with a comma between each item in the list. 

Start by adding a list of players to your program.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
players = ['Harry', 'Hermione']

--- /code ---

--- /task ---

--- task ---

Add this code to print your `players` variable:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
players = ['Harry', 'Hermione']
print(players)

--- /code ---

--- /task ---

--- task ---

You can get to an item in the list by adding its position in square brackets after the variable name.

The first item in the list is at __position 0__. This is different to Scratch, which starts at position 1.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4-5
---
players = ['Harry', 'Hermione']
print(players)

print(players[0])
print(players[1])

--- /code ---

--- /task ---




