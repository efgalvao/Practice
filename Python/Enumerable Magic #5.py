"""
ask

Create a function called one that accepts two params:

    a sequence
    a function

and returns true only if the function in the params returns true for exactly one (1) item in the sequence. 
"""
def one(sq, fun): 
    def one(sq, fun): 
    times = 0
    for n in sq:
        if fun(n) == True:
            times += 1
    if times == 1:
        return True
    else:
        return False