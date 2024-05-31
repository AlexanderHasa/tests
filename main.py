def divide_numbers(x: float | int, y: float | int) -> str:
    if y == 0:
        result = 'cannot divide by 0'
    else:
        result = x / y

    return str(result)


def add_numbers(x: float | int, y: float | int) -> str:
    return str(x + y)


print(divide_numbers(5, 2))
print(divide_numbers(5, 0))
print(divide_numbers(2, 8))
print(add_numbers(2, 8))
