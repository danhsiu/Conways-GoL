# Conways Game of Life on Python

According to "https://conwaylife.com/wiki/Conway%27s_Game_of_Life", Conway's Game of Life (GoL) is "actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players. One interacts with the Game of Life by creating an initial configuration and observing how it evolves."

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. **Underpopulation/Exposure:** Any live cell with fewer than two live neighbours dies.
2. **Overpopulation/Overcrowding:** Any live cell with more than three live neighbours dies.
3. **Stasis:** Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. **Reproduction:** Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.

## Objectives

**We need to implement Conway's GoL in 64-bit integer space (2^64-1). But what happens if we need more integer-space?**

Since Python can store arbitrarily large integers only bounded by system RAM lets use Python as a testbed. We could use 'long long' in C++/C, but any board space larger would not fit on CPU registry size (x64).

## Interesting follow-ups to think about!

1. **What happens if the input file is 1tb? How can we import that into memory? Can we use generators to output graphics in realtime and throw-out old garbage values for that instant?** 
    * If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells!
2. **Say we use Conway's GoL similar to a weather-forecasting simulator where a small input needs to be ran to produce a coherent picture of what happens over 1-million years of compute time. In this case, what would happen if we need even MORE integer space? What would this look like in a multi-GPU/multi-CPU exascale environment?**
    * Perhaps we could use an HPC MPI Job Schedulers (e.g., SLURM, MPICH, MVAPICH, OpenMPI), WareWulf (cluster manager) to manage the configuration an exascale-large board simulation! Perhaps we could use database sharding to store fragments of the board space (e.g., Percona XtraDB Cluster, MariaDB Galera Cluster, Vitess row caching)!
3. **Can we make this game into potentially a benchmarking tool :)?**

