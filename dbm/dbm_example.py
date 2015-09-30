import dbm

with dbm.open("dictionary.txt", "c") as file_1:
    file_1['first'] = "{1:'one', 2:'two'}"

with dbm.open("dictionary.txt") as file_2:
    print(file_2['first'].decode())
