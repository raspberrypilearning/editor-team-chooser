## Choose a random player

Instead of printing a player from one fixed position, pick a random player from your list using `choice`.

Keep your `players` list, but replace `print(players[2])` with code that uses `choice` to select and print a random player.

```python filename="main.py" line_numbers="true" line_number_start="1" line_highlights="1,4-5"
from random import choice  # lets you pick a random item from a list

players = ['Aisha', 'Kai', 'Linh', 'Mateo', 'Noor', 'Zuri']
player = choice(players)  # choose one random player
print(player)  #  show the chosen player
```

## Now run your code

Run your program a few times. You should see **different names** appear.
