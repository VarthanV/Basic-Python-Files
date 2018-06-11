with open('pi.txt') as file:
    line=file.readlines()
    for lines in line:
        print(lines)
    string=''
    for lines in line:
        string+=lines.strip()
    print(lines)
    print(string)    
    print(str(len(string)))
    print(string,end='')
    print(len(string),end='')