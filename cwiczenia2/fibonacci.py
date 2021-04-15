def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def fibonacci_dynamicznie(n):
    f0 = 0
    f1 = 1
    for i in range(0, n + 1):
        if i > 1:
            f = f0 + f1
            f0 = f1
            f1 = f
        else:
            f = i
    return f


def fibonacci_ogonowo(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    print("n=", n, "a=", a, "b=", b)
    return fibonacci_ogonowo(n - 1, b, a + b)


def fib(n):
    return fibonacci_ogonowo(n, 0, 1)


print(fibonacci(6))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(-6))
print(fibonacci_dynamicznie(6))
print(fib(6))
