import os

fd1 = os.open("Example.txt", os.O_CREAT | os.O_APPEND | os.O_WRONLY)
print("fd1:", fd1)
file1 = os.fdopen(fd1, "w+")
file1.write("Hello world!")
file1.flush()
os.close(fd1)
