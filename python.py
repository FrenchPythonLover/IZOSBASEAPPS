try:
    arg = args[1]
    try:
        with open(args[1],"r+") as file:
            try:
                exec(file.read())
            except Exception as e:
                print("[red bold]ERROR:",e)
    except:
        print("[red bold]file does not exist !")
except:
    running = True
    print("Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on IZOS")
    print("Type exit() to exit the interpreter")
    while running:
        com = input(">>> ")
        if com == "exit()":
            print("Bye !")
            running = False
        else:
            try:
                exec(com)
            except Exception as e:
                print(e)