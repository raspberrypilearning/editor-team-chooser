<h2 class="c-project-heading--task">Choose a random player</h2>

--- task ---
Instead of printing a player from one fixed position, pick a random player from your list using `choice`.
--- /task ---

--- task ---
Keep your `players` list, but replace `print(players[2])` with code that uses `choice` to select and print a random player.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1,4-5
---
from random import choice  # lets you pick a random item from a list

players = ['Aisha', 'Kai', 'Linh', 'Mateo', 'Noor', 'Zuri']
player = choice(players)  # choose one random player
print(player)  #  show the chosen player
--- /code ---
</div>
--- /task ---

--- task ---
### Test
Run your program a few times. You should see **different names** appear.
--- /task ---
