while True:
    x = str(input("Input text here for filename conversion.\n"))
    x = x.replace(" ", "_")
    x = x.replace("*", "-")
    x = x.replace(".", "-")
    x = x.replace('"', "'")
    x = x.replace("/", "_")
    x = x.replace("\\", "_")
    x = x.replace("[", "-")
    x = x.replace("]", "-")
    x = x.replace(":", "-")
    x = x.replace(";", "-")
    x = x.replace("|", "")
    x = x.replace("=", "_")
    x = x.replace(",", "0")
    if len(x) > 255:
        x = x[:254]
    print(x+"\n")
