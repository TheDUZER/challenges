def caketime():
        while True:
                while True:
                        try:
                                x = int(input("How old are you in years?\n"))
                                break
                        except ValueError:
                                print("\nThat's not a number. Please use Arabic numerals.\n")
                                continue
                if x >= 25:
                        print ("\nYou are a KURISUMASU KEEKI. You can never get married.\n")
                        continue
                if x < 25:
                        print ("\nThat's great! You can still get married!\n")
                        continue
                else:
                        print("\nWhat was that?\n")
                        continue
caketime()
