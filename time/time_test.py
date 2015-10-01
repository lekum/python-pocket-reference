from timeit import timeit

stmt = "from imp import reload as rl"
res = timeit(stmt=stmt, number=10)
print(res)
