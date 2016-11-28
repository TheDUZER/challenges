with open("words.txt", "r") as words:
    d = []
    for line in words:
        d.append(line)
d = [x.replace('\n', '') for x in d]

n = 0
for x in d:
    y = x[::-1]
    if y == x:
        n = n + 1
        print(x)
    if x == d[-1]:
        print(n)
