#!/usr/bin/env python

from mpi import *

mpi_init(0, [])

proc  = mpi_comm_rank(MPI_COMM_WORLD)
nproc = mpi_comm_size(MPI_COMM_WORLD)

print(f"Process {proc}/{nproc}")

mpi_barrier(MPI_COMM_WORLD)

# Stage 1, synchronous send/recv
if proc == 0:
	ab = b"MY RANK IS "

	for i in range(1, nproc):
		a = ab + str(i).encode()
		print(f"\nSending  from 0 to {i}: {a}")
		mpi_send(a, len(a), MPI_CHAR, i, 0, MPI_COMM_WORLD)
		c = mpi_recv(16, MPI_CHAR, i, 1, MPI_COMM_WORLD)
		print(f"Received from {proc} to 0: {b''.join(c)}")
else:
	b = mpi_recv(16, MPI_CHAR, 0, 0, MPI_COMM_WORLD)
	b = b''.join(b)
	print(f"Received from 0 to {proc}: {b}")
	b = b.lower()
	mpi_send(b, len(b), MPI_CHAR, 0, 1, MPI_COMM_WORLD)
	print(f"Sent     from {proc} to 0: {b}")

mpi_barrier(MPI_COMM_WORLD)

if proc == 0:
	print("\nStage 1 complete, all responses in\n")

mpi_barrier(MPI_COMM_WORLD)

mpi_finalize()

if proc == 0:
	print("\ndone\n")
	print("If you didn't see any errors above, then the test was a success.\n")
