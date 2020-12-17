import algorithm
import numpy as np

def test_algorithm():

	# General test-case.
	zeros = np.zeros((10,10,10))
	zeros[5,5,:] = 1
	row, column = algorithm.Algorithm(zeros)

	assert(row.mean() == 5)
	assert(column.mean() == 5)