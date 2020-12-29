def count_trees(map, i, j):
    trees = 0
    x,y = (0, 0)
    maximumX = len(map[0])
    while y < len(map) - 1:
        x += i
        y += j
        if x >= maximumX:
            x = x - maximumX
        if map[y][x] == "#":
            trees += 1
    return trees

with open("C:\input3.txt") as f:
    input = f.readlines()

input = [x.strip() for x in input]

trees1 = count_trees(input, 1,1)
trees2 = count_trees(input, 3, 1)
trees3 = count_trees(input, 5, 1)
trees4 = count_trees(input, 7, 1)
trees5 = count_trees(input, 1, 2)
print(trees1*trees2*trees3*trees4*trees5)




