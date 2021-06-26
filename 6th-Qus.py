# 6 - Write a function that will take a string s as input and return whether s contains all letters of the alphabet (a to z) or not. It should return true for sentences
# like "The quick brown fox jumps over the lazy dog".


def alphabet(word):
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    for i in alphabets:
        if i not in word.lower():
            return False
    return True


print(alphabet("hello"))
print(alphabet("The quick brown fox jumps over the lazy dog"))
