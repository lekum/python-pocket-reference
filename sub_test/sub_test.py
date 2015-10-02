from subprocess import call, Popen, PIPE, check_output

print(call("ls -l", shell=True))
print(check_output("ls -l", shell=True).decode())
pipe1 = Popen("ls -l", stdout=PIPE, shell=True)
pipe2 = Popen("wc -l", stdin=pipe1.stdout, stdout=PIPE, shell=True)
print(pipe2.stdout.read().decode())
