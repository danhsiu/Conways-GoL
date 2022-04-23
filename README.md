# Conway's Game of Life on Python
## Objectives & Approach

**We need to implement Conway's GoL in 64-bit integer space!**

1. To create a program to play Conway's GoL, we can use Python3 as a testbed for exploring algorithmic solutions! Since Python can store arbitrarily large integers only bounded by system RAM it serves as an easy language for starters.
     
     
     *We could use C/C++, though any board space larger that 64-bit space would not fit on modern CPU registry size (x64). We could use a library like [GMP](https://gmplib.org/) to accept arbitrary precision integers for future development.*

A trivial solution following the execution of Conway's GoL can be found in the "1. Python/ConwaysGoL.ipynb" folder. 


## Interesting follow-ups to think about!

1. **What happens if the input file is 1TB? How can we import that into memory? Can we use generators to output graphics in realtime and throw-out old garbage values for that instant?** 
    * If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells! 
2. **Say we use Conway's GoL similar to a weather-forecasting simulator where a small input needs to be ran to produce a coherent picture of what happens over 1-million years of compute time. In this case, what would happen if we need even MORE integer space? What would this look like in a multi-GPU/multi-CPU exascale environment?**
    * Perhaps we could use an HPC MPI Job Schedulers (e.g., SLURM, MPICH, MVAPICH, OpenMPI), WareWulf (cluster manager) to manage the configuration an exascale-large board simulation! Perhaps we could use database sharding to store fragments of the board space (e.g., Percona XtraDB Cluster, MariaDB Galera Cluster, Vitess row caching)!
3. **Can we make this game into potentially a benchmarking tool :)?**

