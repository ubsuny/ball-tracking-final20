import numpy as np 

def Algorithm(MATRIX):
    
    maxDim = len(MATRIX)
    z = np.arange(maxDim)
    tmax = len(MATRIX[1,1,:])
    row = np.zeros(tmax)
    column = np.zeros(tmax)
    
    for i in range(tmax):
        row[i] = sum(np.dot(z,MATRIX[:,:,i]))
        column[i] = np.sum(np.dot(MATRIX[:,:,i],z))
        
    return row, column