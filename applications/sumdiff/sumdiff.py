"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

num_store = {}

# run our function on all numbers in our set and store them in our dict so we can subscript over it
for ind in q:
    if ind not in num_store:
        num_store[ind] = f(ind)
sort_store = sorted(num_store.items())
print(sort_store)

adds = {}
subs = {}

# these for loops will perform operations on tuple pairs of each possible combination in q. ie. (1,10),(2,14),etc.
# for each pair that we have, we will create an instance of them for both our add and sub dict and save the values we receive from calling the functions on them
for ind in range(len(sort_store)):
    #NOTE: sort_store[ind][0] will reference the first object in a pair. this is the number we receive from q. sort_store[ind][1] will be the result from the function
    q_ref = sort_store[ind][0]
    fun_res = sort_store[ind][1]
    # this will give us the result of adding a + a
    adds[q_ref, q_ref] = fun_res + fun_res

    # this second for loop will give results of adding a + b
    for sec in range(len(sort_store)):
        sec_ref = sort_store[sec][0]
        sec_res = sort_store[sec][1]

        adds[q_ref, sec_ref] = fun_res + sec_res

    # then we check for our subtractions
    if ind != sec and sec < len(sort_store):
        subs[sec_ref, q_ref] = sec_res - fun_res

# items will return a tuple view of the specified items
# so we will compare the second position of the tuples we get from adds and subs which will be our values.
# if the values are the same, we can print/return the first index to show the comparison of which combinations are the same.
for pos in adds.items():
    for neg in subs.items():
        if pos[1] == neg[1]:
            print(f'f({pos[0][0]}) + f({pos[0][1]}) = f({neg[0][0]}) - f({neg[0][1]})')