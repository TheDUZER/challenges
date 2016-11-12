#By Ian the Impaler 10/6/2016
print("Welcome to Ian's FIZZBUZZ dawg. Press enter to begin.")
input()
x = range(1, 101)
i = 0
def fizzbuzz():
  if x[i] % 3 == 0 and x[i] % 5 == 0:
    print ("fizzbuzz")
  elif x[i] % 3 == 0:
    print("fizz")
  elif x[i] % 5 == 0:
    print("buzz")
  else:
    print(x[i])          
while i < 100:
  fizzbuzz()
  i = i + 1
print("Calculation Complete")
while True:
  a = input("Type 'again' to repeat. Type 'finished' to close the program.\n")
  if 'again' in a:
    i = 0
    while i < 100:
      fizzbuzz()
      i = i + 1
    print("Calculation Complete")
  elif 'finished' in a:
    exit()
  else:
    print("Invalid command.")
    continue
