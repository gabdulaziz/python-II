def fibonacci_decorator(func):
    memo = {}
    def wrapper(n):
        if n in memo:
            return memo[n]
        result = func(n)
        memo[n] = result
        return result
    return wrapper

@fibonacci_decorator
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(0))   # 0
    print(fibonacci(1))   # 1
    print(fibonacci(6))   # 8
    print(fibonacci(10))  # 55