<h2 class="c-project-heading--task">Choose a random player</h2>

--- task ---
Pick a random player from your list using `choice`.
--- /task ---

--- task ---
Import `choice` and use it to select a random player.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1,4
---
from random import choice  # lets you pick a random item from a list

players = ['Harry', 'Hermione', 'Neville', 'Ginny', 'Luna', 'Ron']
player = choice(players)  # choose one random player
print(player)
--- /code ---
</div>
--- /task ---

--- task ---
### Test
Run your program a few times. You should see **different names** appear.
--- /task ---
