##Generate dictionary:

doors = {}

for x in range(1, 101):
    doors[x] = "open"

##Initial iteration variable
y = 1

##Toggles doors open and closed depending on current state
def toggle():
    for x in doors:
        x = x * y
        try:
            if doors[x] == "open":
                doors[x] = "closed"
            elif doors[x] == "closed":
                doors[x] = "open"
        ##Catches error when result of x * y goes over doors max index
        except KeyError:
            continue

##Main Loop        
while True:
    toggle()
    ##Iteration counter
    y = y + 1
    if y == 101:
        break
print(doors)
print('\n')

##Displays open doors
print("open doors: ", end='')
for x in doors:
    if doors[x] == "open":
        print(str(x) + ", ", end='')
print('\n')

##Displays closed doors
print('closed doors: ', end='')
for x in doors:
    if doors[x] == "closed":
        print(str(x) + ", ", end='')
print('\n')
