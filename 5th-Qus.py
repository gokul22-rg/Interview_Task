
#5 - Write a function that will take a file name fname and a string s as input. It will return whether s occurs
     #inside the file. It's possible that the file is extremely large so it cannot be read into memory in one shot.

def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def search_file(filename, string):
    with open(filename) as f:
        for piece in read_in_chunks(f):
            if string in piece:
                print("The given string is present in the file")
            else:
                print("The given string is not in the file")


search_file("test.txt", "Hello")

