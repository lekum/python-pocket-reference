import os.path

path1 = "~/tmp/"
exp_path1 = os.path.expanduser(path1)
if not os.path.isdir(exp_path1):
    os.mkdir(exp_path1)
