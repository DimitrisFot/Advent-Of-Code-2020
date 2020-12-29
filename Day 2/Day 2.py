with open("C:\input2.txt") as f:
    passwords = f.readlines()

sum = 0

#for line in passwords:
#    temp = line.split("-")
#    minvalue = temp[0]
#    temp = temp[1].split()
#    maxvalue = temp[0]
#    restriction = temp[1]
#    restriction = restriction[0]
#    password = temp[2]
#    if password.count(restriction) <= int(maxvalue) and password.count(restriction) >= int(minvalue):
#        sum += 1

for line in passwords:
    temp = line.split("-")
    pos1 = int(temp[0]) - 1
    temp = temp[1].split()
    pos2 = int(temp[0]) - 1
    restriction = temp[1]
    restriction = restriction[0]
    password = temp[2]

    foo = ([pos for pos, char in enumerate(password) if char == restriction])
    if (((pos1 in foo) and (pos2 not in foo)) or ((pos1 not in foo) and (pos2 in foo))):
        sum += 1

print(sum)