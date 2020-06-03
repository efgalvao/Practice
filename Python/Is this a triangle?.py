"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.
"""
def is_triangle(a, b, c):
    return abs(b - c) < a and a < (b + c) 
    #or (( a - c ) < b and b < (a + c)) or ((a - b) < c and c < (a + b))

print(is_triangle(1, 2, 3))