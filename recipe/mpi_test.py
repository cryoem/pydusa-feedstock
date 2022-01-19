#!/usr/bin/env python

from mpi import *

mpi_init(0, [])

proc  = mpi_comm_rank(MPI_COMM_WORLD)
nproc = mpi_comm_size(MPI_COMM_WORLD)

print(f"Process {proc}/{nproc}")

mpi_barrier(MPI_COMM_WORLD)
mpi_finalize()

if proc == 0:
	print("\ndone\n")
	print("If you didn't see any errors above, then the test was a success.\n")
