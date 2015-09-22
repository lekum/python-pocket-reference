import os


if __name__ == '__main__':

    dir = 'build/bin'
    if not os.path.isdir(dir):
        os.makedirs(dir)
    os.chdir(dir)
    with open("Example.txt", "w") as file1:
        file1.write("Hello world!")
    os.chdir("..")
    if not os.path.islink("Example.txt"):
        os.symlink("bin/Example.txt", "Example.txt")
    os.chdir("..")
    for (dirpath, dirnames, filenames) in os.walk("."):
        print("Current dir:",dirpath)
        print("Files:", " ".join(filenames))
        print("Dirs:", " ".join(dirnames))
        print("****")
