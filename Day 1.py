with open("C:\input.txt") as f:
    input = f.readlines()

input = [int(numeric_string) for numeric_string in input]

a = 0
b = 0

for i in input:
    for j in input:
        if i+j == 2020:
            a = i
            b = j
            break



print (a,b, a*b)