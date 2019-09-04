"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open("foo.txt") as fooFile:
    for line in fooFile:
        print(line, end="")
    fooFile.close()

print("\n")  # Line break to visually separate next output


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open("bar.txt", "w") as barFile:
    barFile.write("Line One\n")
    barFile.write("Line Two\n")
    barFile.write("Line Three\n")
    barFile.close()

with open("bar.txt") as barFile:
    for line in barFile:
        print(line, end="")
    barFile.close()
