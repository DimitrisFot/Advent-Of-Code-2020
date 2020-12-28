all_seats = [int(
    (l.replace('B','1').replace('F','0')
    .replace('R','1').replace('L','0'))
    ,2) for l in open("C:\input5.txt")]

print(all_seats)
print(max(all_seats))

your_seat = [s for s in range(min(all_seats), max(all_seats))if s not in all_seats][0]
print(your_seat)
print("Test")