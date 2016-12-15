# s = [99]*10**6*5
# %timeit -n 2 -r 100 square_fun(s)
#
# .append
# 2 loops, best of 100: 583 ms per loop
#
# pre-allocate
# 2 loops, best of 100: 476 ms per loop
#
# pre-append
# 2 loops, best of 100: 364 ms per loop
#
# list comprehension
# 2 loops, best of 100: 329 ms per loop
#
# map
# 2 loops, best of 100: 584 ms per loop
#
# cython list comprehension
# 2 loops, best of 100: 199 ms per loop
#

'''
# .append
def square_fun(seq):
    squares = []
    for x in seq:
        squares.append(x**2)


# pre-allocate
def square_fun(seq):
    squares = [None]*len(seq)
    for i,x in enumerate(seq):
        squares[i] = x**2
        

# pre-append
def square_fun(seq):
    squares = []
    squares_app = squares.append
    for x in seq:
        squares_app(x**2)


#list comprehension
def square_fun(seq):
    squares = [x**2 for x in seq]

'''
# map
def square_fun(seq):
    squares = map(lambda x: x**2, seq)
    
