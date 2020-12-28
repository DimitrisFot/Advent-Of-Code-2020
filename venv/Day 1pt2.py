with open("C:\input.txt") as f:
    input = f.readlines()

input = [int(numeric_string) for numeric_string in input]

a = 0
b = 0
c = 0

for i in input:
    for j in input:
        for k in input:
          if i+j+k == 2020:
            a = i
            b = j
            c = k
            break



print (a,b,c, a*b*c)