#!/usr/bin/env python
# coding: utf-8

# # Project: Linear Regression
# _Linear Regression_ is when you have a group of points on a graph, and you find a line that approximately resembles that group of points. A good Linear Regression algorithm minimizes the _error_, or the distance from each point to the line. A line with the least error is the line that fits the data the best. We call this a line of _best fit_.
# We will use loops, lists, and arithmetic to create a function that will find a line of best fit when given a set of data.

# ## Part 1: Calculating Error
# The line we will end up with will have a formula that looks like:
# y = m*x + b

# `m` is the slope of the line and `b` is the intercept, where the line crosses the y-axis.

# Fill in the function called `get_y()` that takes in `m`, `b`, and `x`. It should return what the `y` value would be for that `x` on that line! 

def get_y(m, b, x):
    y = m*x+b
  pass

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

 
# Reggie wants to try a bunch of different `m` values and `b` values and see which line produces the least error. To calculate error between a point and a line, he wants a function called `calculate_error()`, which will take in `m`, `b`, and an [x, y] point called `point` and return the distance between the line and the point.
 
# To find the distance:
# 1. Get the x-value from the point and store it in a variable called `x_point`
# 2. Get the y-value from the point and store it in a variable called `y_point`
# 3. Use `get_y()` to get the y-value that `x_point` would be on the line
# 4. Find the difference between the y from `get_y` and `y_point`
# 5. Return the absolute value of the distance (you can use the built-in function `abs()` to do this)
 
# The distance represents the error between the line `y = m*x + b` and the `point` given.
 
def calculate_error(m,b,point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y-y_point)
    return distance


print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_error(m,b,points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m,b,point)
        total_error +=point_error
    return total_error


#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))


# Our next step is to find the `m` and `b` that minimizes this error, and thus fits the data best!


# ## Part 2: Try a bunch of slopes and intercepts!

possible_ms = [m * 0.1 for m in range(-100,101)]
possible_bs = [b * 0.1 for b in range(-200,201)]

 
# First, create the variables that we will be optimizing:
# * `smallest_error` &mdash; this should start at infinity (`float("inf")`) so that any error we get at first will be smaller than our value of `smallest_error`
 
# * Iterate through each element `m` in `possible_ms`
# * For every `m` value, take every `b` value in `possible_bs`
# * If the value returned from `calculate_all_error` on this `m` value, this `b` value, and `datapoints` is less than our current `smallest_error`,
# * Set `best_m` and `best_b` to be these values, and set `smallest_error` to this error.
# 
# By the end of these nested loops, the `smallest_error` should hold the smallest error we have found, and `best_m` and `best_b` should be the values that produced that smallest error value.
# 
# Print out `best_m`, `best_b` and `smallest_error` after the loops.
# 
# 



datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m,b,datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
print(best_m,best_b,smallest_error)

# Using this `m` and this `b`, what does your line predict the bounce height of a ball with a width of 6 to be?
# In other words, what is the output of `get_y()` when we call it with:
# * m = 0.3
# * b = 1.7
# * x = 6

# In[10]:


get_y(0.3, 1.7, 6)


# Our model predicts that the 6cm ball will bounce 3.5m.




