def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return 0
    elif n == 0:
        print(f"{n}: {0}")
        return 0
    elif n == 1 or n == 2:
        print(f"{n}: {1}")
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(f"{n}: {result}")
        return result

print(fibonacci(4))
