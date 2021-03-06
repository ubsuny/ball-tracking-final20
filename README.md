# Ball tracking

## Project Outline
Develop your own code based on linear algebra to track a ball in a sequence of pictures.
See: https://www.youtube.com/watch?v=PfOJhxm3M8U

- Generate a timesequence of a 3 dimensional dataset (2 spatial 1 time), of a "Ball" moving.
- Develop an algorithm based on Linear Algebra (Matrix operations) to track the position of the ball in time.

## How to run the code
The juypter notebook BallTracking.ipynb and the python file algorithm.py, contains all the code for this project and outlines an example.  To run the notebook, one need only have access to basic python libraries which include matplotlib, math, and numpy libraries.

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

Some error is evident in this system. This is due to the fact that to make a continuous number line fit into a discrete matrix, we rounded the x and y coordinates down in order to have them fit in a matrix box. Each matrix box is an integer value, so the decimal of the coordinates was erased. This however gives us a well defined maximum average error of 0.5, half the size of a matrix box, across the board. However, the maximum error possible for a single box is .99999 repeating, as we rounded down to the nearest integer in constructing the matrix.
