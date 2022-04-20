# With the use of a recursive function, this script generates
# the sequence of the fibonacci series (Fn = Fn-1 + Fn-2) for
# the specified range in the input


def fibo(n):
    if n == 1:
        return n
    elif n == 0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


num = int(input("Input a positive integer: "))

if num < 0:
    raise TypeError("Only positive numbers allowed")
else:
    print("Fibonacci sequence: ")
    for i in range(0, num):
        print(fibo(i))
