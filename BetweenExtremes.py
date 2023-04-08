def between_extremes(numbers):
    #Your code goes here!
    minn = min(numbers)
    maxx = max(numbers)
    return maxx-minn


numbers = [23, 3, 19, 21, 16]
print(between_extremes(numbers))