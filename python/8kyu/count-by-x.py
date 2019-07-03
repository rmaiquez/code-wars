# Create a function with two arguments that will return a list of length (n) with multiples of (x).

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array (or list in Python, Haskell or Elixir).

# Examples:

# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]

# My Solution:

def count_by(x, n):
  my_list = [] #start with an empy list
  for i in range(n):
    #notice i+1 in the line below
    my_list.append((i+1) * x) #multiply current index i+1 by x
  return my_list

# Clever Solution:

def count_by(x, n):
    return range(x, x * n + 1, x)
