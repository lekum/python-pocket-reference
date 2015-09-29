import re

input_string = "hello world! hello my friend"
pobj = re.compile('hello[\s]*(?P<what>\w+)')
for idx, mobj in enumerate(pobj.finditer(input_string)):
    print(idx, ':', mobj.group("what"))
