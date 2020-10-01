exps_dict = {}


def expensive_seq(x, y, z):
    # check to see if it's already in the dictionary. if it is, just return it so we don't run through all the code and recursions.
    if (x, y, z) in exps_dict:
        return exps_dict[(x, y, z)]

    # start our running total
    total = 0
    # if x has reached 0 or less than 0, then y and z will be our total for this computation
    if x <= 0:
        total = y + z
    # otherwise, run recursion on the function as determined by the project directions
    elif x > 0:
        total = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    # once we have our total, set that as the value using our key of x,y,z to help with future calls in the cycle
    exps_dict[(x, y, z)] = total
    return total

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
