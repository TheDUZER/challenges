##Algorithm to generate dictionary:
##for x in range(1,101):
##    print(str(x) + ': "open", ', end='')
doors = {1: "open", 2: "open", 3: "open", 4: "open", 5: "open", 6: "open", 7: "open", 8: "open", 9: "open", 10: "open", 11: "open", 12: "open", 13: "open", 14: "open", 15: "open", 16: "open", 17: "open", 18: "open", 19: "open", 20: "open", 21: "open", 22: "open", 23: "open", 24: "open", 25: "open", 26: "open", 27: "open", 28: "open", 29: "open", 30: "open", 31: "open", 32: "open", 33: "open", 34: "open", 35: "open", 36: "open", 37: "open", 38: "open", 39: "open", 40: "open", 41: "open", 42: "open", 43: "open", 44: "open", 45: "open", 46: "open", 47: "open", 48: "open", 49: "open", 50: "open", 51: "open", 52: "open", 53: "open", 54: "open", 55: "open", 56: "open", 57: "open", 58: "open", 59: "open", 60: "open", 61: "open", 62: "open", 63: "open", 64: "open", 65: "open", 66: "open", 67: "open", 68: "open", 69: "open", 70: "open", 71: "open", 72: "open", 73: "open", 74: "open", 75: "open", 76: "open", 77: "open", 78: "open", 79: "open", 80: "open", 81: "open", 82: "open", 83: "open", 84: "open", 85: "open", 86: "open", 87: "open", 88: "open", 89: "open", 90: "open", 91: "open", 92: "open", 93: "open", 94: "open", 95: "open", 96: "open", 97: "open", 98: "open", 99: "open", 100: "open"}

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
