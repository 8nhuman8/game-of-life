# Game of Life

`The Python implementation of the most famous cellular automaton called "Game of Life" devised by the British mathematician John Horton Conway in 1970`

<p align="center">
  <img src="docs/README/demo.gif" alt="Game of Life Demo">
</p>

## Table of contents

- [Brief information about the Game of Life](#brief-information-about-the-game-of-life)
- [Usage and installation](#usage-and-installation)
- [Credits and references](#credits-and-references)
- [License](#license)

## Brief information about the Game of Life

> The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.
> The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

> 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
> 2. Any live cell with two or three live neighbours lives on to the next generation.
> 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
> 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

> These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

> 1. Any live cell with two or three live neighbours survives.
> 2. Any dead cell with three live neighbours becomes a live cell.
> 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

> The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

## Usage and installation

1. Upgrade required packages with `pip install -r requirements.txt --upgrade` (if you don't have one, it will be automatically installed).
2. Run the `main.py` with `python src/main.py`.

## Credits and references

[Wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) about this cellular automata.

## License

[Game of Life](https://github.com/8nhuman8/game-of-life) specific code is distributed under [MIT License](https://github.com/8nhuman8/game-of-life/blob/master/LICENSE).

Copyright (c) 2020 Artyom Bezmenov
