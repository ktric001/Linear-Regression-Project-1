# Linear-Regression-Project-1
First Attempt at Linear Regression

The following project creates a function that will follow a line of best fit when given a set of data.

Function 1: Get_y(m,b,x)

This function gets y from the inputs m,b, and x. This is a super normal slope intercept equation.

Function 2: calculate_error(m,b,point)

This function uses the data point given and inputs it into the same intercept equation. Then we calculate the absolute distance between this y and the y from Get_y.

Function 3: calculate_all_error(m,b,points)

This function iterates over the datapoints, and runs over the calculate_error function. It then adds these point_errors to total_error.

Last step: Finding the smallest error

Here, we create a list of possible ms and bs. Then, we iterate over these lists, and calculate the smallest error in order to find the best m, b, and smallest error.

