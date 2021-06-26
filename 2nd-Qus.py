
# 2 - Write a function in python that will take a list of numbers n as input and return
       # the largest 2 elements in the list. Don't use the sort method.


n = [10, 20, 90, 50, 80]
def largestElement(n):
    first_largest = max(n[0], n[1])
    second_largest = min(n[0], n[1])


    for i in range(2 ,len(n)):
        if n[i] > first_largest:
            second_largest = first_largest
            first_largest =n[i]

        elif n[i] > second_largest:
            second_largest = n[i]

    return first_largest, second_largest


print("Largest 2 Elements in the list :", largestElement(n))
