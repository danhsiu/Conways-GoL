# Conways-GoL

Here we implement Conway's game of life in 64-bit integer space (2^64-1). According to "https://conwaylife.com/wiki/Conway%27s_Game_of_Life", Conway's Game of Life is "actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players. One interacts with the Game of Life by creating an initial configuration and observing how it evolves."

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    1. Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure).
    2. Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
    3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
    4. Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.
