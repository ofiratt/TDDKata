# Minesweeper TDD Kata

Assume the input is valid and playing occur only after the setup

![alt text](https://raw.githubusercontent.com/ofiratt/TDDKata/master/Minesweeper/assets/class-api.png)


###Requirements

- createField - Create a new empty field (without mines)
- layMine - Lay mine in selected cell (row, col)
- play - Reveal the selected cell (row, col) using the *[flood fill algorithm](https://en.wikipedia.org/wiki/Flood_fill)*
- status - Return the game status => WIN, LOST, PLAYING
- printField - Print to screen the mine field 
  - Not revealed cell - “.”
  - Mine cell - “*”
  - Empty cell - “+“
  - Number cell - “1” or “2” …
  
  
### Game Examples:

Wining short game:  
```python
# game setup
game = Minesweeper()
game.createFeild(3,3)
game.layMine(0, 0)

# game play
game.printField();
". . ."
". . ."
". . ."


game.play(0, 2)
game.printField();
"* 1 +"
"1 1 +"
"+ + +"

game.status();
"WIM"
```

Losing short game:
```python
# game setup
game = Minesweeper()
game.createFeild(3,3)
game.layMine(0, 0)
game.layMine(1, 1)

# game play
game.printField();
". . ."
". . ."
". . ."

game.status();
"PLAYING"

game.play(0, 0)
game.printField();
"* . ."
". * ."
". . ."

game.status();
"LOST"
```

[Full wining game example](/WINNIG_GAME_EXAMPLE)


