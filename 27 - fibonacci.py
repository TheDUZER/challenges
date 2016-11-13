def fib(n):
    a = 0
    b = 1
    while a < n:
        print (a)
        a = b
        b = a + b
while True:
    fib(int(input()))
    a = input("Any key to continue")
    if a == 'quit':
        quit()
