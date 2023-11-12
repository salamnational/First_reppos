def square_sum(numbers):
    square = []
    for i in numbers:
        square.append(i**2)
    return sum(square)