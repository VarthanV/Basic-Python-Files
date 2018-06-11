file='py.txt'
with open(file) as files:
    a=files.readlines()
    for line in a:
        print(line)