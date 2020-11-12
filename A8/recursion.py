def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def bunny_ears(bunnies):
    if bunnies == 0:
        return 0
    return 2 + bunny_ears(bunnies - 1)


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(factorial(int(input())))
    print(bunny_ears(int(input())))
    

if __name__ == '__main__':
    main()
