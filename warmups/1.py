#-------------------- fibonacci --------------------

# beginner
def fibSeq(n: int) -> None:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a,b = b, a + b
fibSeq(10)

print("\n")

# recursive
# The recursive function is not efficient for large n due to exponential time complexity.
def recursive_fib(n: int)-> int:
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

n = 10
for i in range(n):
    print(recursive_fib(i), end=" ")

print("\n")

# memoized
memo = {}
def recursive_fib(n: int)-> int:
    if n in memo:
        return memo[n]
    
    if n == 0 :
        result = 0
    elif n == 1 :
        result = 1
    else:
        result = recursive_fib(n-1) + recursive_fib(n-2)
    memo[n] = result
    return result

n = 10
for i in range(n):
    print(recursive_fib(i), end=" ")

print("\n")

# generator function
def fib_generator():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b
n = 10
gen = fib_generator()
for _ in range(10):
    print(next(gen), end=" ")






         
