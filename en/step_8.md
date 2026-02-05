## Odd players

Let's improve your program to work with an odd number of players.

--- task ---

+ Add another name to your `players.txt` list, so that you have an odd number of players.

--- code ---
---
language: python
filename: players.txt
line_numbers: true
line_number_start: 1
line_highlights: 5
---
Harry
Hermione
Neville
Ginny
Luna

--- /code ---

--- /task ---

--- task ---

If you test your code, you'll see that you get an error message.

![screenshot](images/error.png)

--- /task ---

The error is because your program keeps choosing random players for team A and then team B. However, if there is an odd number of players then after choosing a player for team A there are no players left to choose from for team B.

--- task ---

To fix this bug, you can tell your program to `break` out of your `while` loop if your `players` list is empty.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 15-16
---
while len(players) > 0:
    player_A = choice(players)
    team_A.append(player_A)
    players.remove(player_A)

    if players == []:
        break
    
    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)

--- /code ---

--- /task ---

--- task ---

If you test your code again, you should see that it now works with an odd number of players.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
Team A ['Harry', 'Ginny', 'Luna']
Team B ['Hermione', 'Neville']

--- /code ---

--- /task ---




