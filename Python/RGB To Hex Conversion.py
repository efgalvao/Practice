"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
"""
def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return ('%02x%02x%02x' % (r, g, b)).upper()

print(rgb(255, 255, 255)) # returns FFFFFF
print(rgb(255, 255, 300)) # returns FFFFFF
print(rgb(0,0,0)) # returns 000000
print(rgb(148, 0, 211)) # returns 9400D3