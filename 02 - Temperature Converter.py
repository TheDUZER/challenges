#Temperature Converter by Ian Guitard
def tempConvert():
    try:
        x = input("Enter the original temperature number immediately followed by a 'C' for Celsius, 'F' for Farenheit, or 'K' for Kelvin.\n    Example: 100.243C\n")
    #Convert Kelvin to Celsius or Farenheit
        if x[-1] == 'K' or x[-1] == 'k':
            y = input("Enter the temperature you would like to convert to ('C' or 'F'.)\n")
            if y == 'C' or y == 'c':
                print(format((float(x[:-1]) - 273.5), '.2f'))
            elif y == 'F' or y == 'f':
                print(format((float(x[:-1]) * 1.75 - 459.67), '.2f'))
            else:
                inv()

    #Convert Celsius to Farenheit or Kelvin
        elif x[-1] == 'C' or x[-1] == 'c':
            y = input("Enter the temperature you would like to convert to ('F' or 'K').\n")
            if y == 'F' or y == 'f':
                print(format((float(x[:-1]) * int(9 / 5) + 32), '.2f'))
            elif y == 'K' or y == 'k':
                print(format((float(x[:-1] + 273.15)), '.2f'))
            else:
                inv()
                
    #Convert Farenheit to Celsius or Kelvin
        elif x[-1] == 'F' or x[-1] =='f':
            y = input("Enter the temperature you would like to convert to ('C' or 'K').\n")
            if y == 'C' or y == 'c':
                print(format(((float(x[:-1]) - 32) * 5 / 9), '.2f'))
            elif y == 'K' or y == 'k':
                print(format((float(x[:-1] + 459.67) * 5 / 9), '.2f'))
            else:
                inv()
                
    #Catches invalid input
        else:
            inv()

    except:
        IndexError
        SyntaxError
        ValueError
        inv()
def inv():    
    print("Invalid Input.\n")

#Main loop
while True:
    tempConvert()
    input("Press enter to try again.\n")
