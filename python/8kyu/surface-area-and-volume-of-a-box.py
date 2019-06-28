# Write a function that returns the total surface area and volume of a box as an array: [area, volume].

# Solution:
def get_size(w,h,d):
    area = 2*(w*h + w*d + d*h)
    volume = w*h*d
    return [area, volume]
