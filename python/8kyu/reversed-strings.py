# Complete the solution so that it reverses the string value passed into it.
#
# solution('world') # returns 'dlrow'

# This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off
# and specifying a step of -1, it reverses a string.

def solution(string):
    return string[::-1]
