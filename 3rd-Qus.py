
#  3 - Write a function in Python that will take a list of numbers n and a number m as inputs and return the
      # largest m numbers in the list n. Don't use the sort method.


def largest(n, m):
    for i in range(m):
        a = max(n)
        print("Largest number  " + str(i + 1) + "-", a)
        n.remove(a)


largest([1, 2, 3, 4, 34, 56, 55], 4)
