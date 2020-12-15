# Ball tracking

Develop your own code based on linear algebra to track a ball in a sequence of pictures.
See: https://www.youtube.com/watch?v=PfOJhxm3M8U

- Generate a timesequence of a 3 dimensional dataset (2 spatial 1 time), of a "Ball" moving.
- Develop an algorithm based on Linear Algebra (Matrix operations) to track the position of the ball in time.

## The Tracking Algorithm

The tracking algorithm was designed to take the matrix from the above simulation and feed out the coordinate in the trajectory matrix of where the ball was located in each time frame.  For each time frame of the square matrix, the ball's single location had a '1' and all other places a zero.  

The algorithm consists of the dot product, carried out in both orders, and summed.  To calculate where the ball's position is located, M being the matrix and z a matrix the size of the length of a side of the square matrix M, then the sum of the dot product of z and M in that order is the row coordinate of the ball, and the sum of the elements of the dot product of M and z in that order is the column coordinate of the ball.

Below is an example of the algorithm:

![](https://github.com/ubsuny/ball-tracking-final20/blob/main/Images/MatrixRow.png)

Above, b represents our square matrix M, and A represents z, a vector with elements numbered 0 to the size of the side of the square matrix M. The result of the dot product of z and M is a column vector containing the number of the row of where the ball is located. Summing this column vectors elements results in the exact single number of the ball's row position.  

![](https://github.com/ubsuny/ball-tracking-final20/blob/main/Images/MatrixColumn.png)

Finding the column of the ball's coordinate is the exact same procedure as finding the row with the one difference of switching the order of the dot product.

Below are the results of an example run, comparing the simulation data to the tracking algorithm:

![](https://github.com/ubsuny/ball-tracking-final20/blob/main/Images/ballComplete.png)
