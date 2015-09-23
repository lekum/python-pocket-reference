import os

if __name__ == '__main__':
    os.execl("/bin/ls", "-l", "/home/")
