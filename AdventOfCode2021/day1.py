ct = 0
with open('./src/input1.txt', 'r') as f:
    lines = [int(line) for line in f.readlines()]

for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i-1]):
        ct += 1
print(ct)

ct = 0
for i in range(0, len(lines)):
    if sum(lines[i:i+3]) < sum(lines[i+1:i+4]):
        ct += 1
print(ct)
