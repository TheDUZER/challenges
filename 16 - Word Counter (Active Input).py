def wordCounter():
    x = input("\nType some stuff. Output will be word count.\n")
    y = x.split(" ")
    if x == '':
        print("0")
    else:
        print(len(y))
        

while True:
    wordCounter()
        
            
