# 1 -  Write a function in python that will take a list of numbers n as input and return the largest element
# in the list. Don't use the sort method.


def largestElement(n):
    max = n[0]
    for x in n:
        if x > max:
             max = x

    return max


n = [10, 20, 90, 50, 80]
print("Largest Element is:", largestElement(n))
