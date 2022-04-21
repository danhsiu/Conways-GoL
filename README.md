# Conways Game of Life on Python, CUDA, and Metal

Here we implement Conway's game of life in 64-bit integer space (2^64-1). According to "https://conwaylife.com/wiki/Conway%27s_Game_of_Life", Conway's Game of Life is "actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players. One interacts with the Game of Life by creating an initial configuration and observing how it evolves."

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure).
2. Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.

## Interesting follow-ups to think about!

1. **What happens if the input file is 1tb? How can we import that into memory? Can we use generators to output graphics in realtime and throw-out old garbage values for that instant?** 
    * If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells!
2. **Say we use Conway's GoL as a forecasting simulator where a small input is needed, and the simulation needs to be ran to produce a coherent picture of what happens over a 1-million years of compute time.** In this case, what would happen if we need even MORE integer space? What would this look like in a multi-GPU/multi-CPU environment?
    * Perhaps we could use an OpenMPI, HPC MPI Job Schedulers (e.g., SLURM, MPICH, MVAPICH), WareWulf (cluster manager) to manage the configuration an exascale-large board simulation! Perhaps we could use database sharding to store fragments of the board space (e.g., Percona XtraDB, MariaDB Galera, Vitess)!
3. **Can we make this game into potentially a benchmarking tool :)?**