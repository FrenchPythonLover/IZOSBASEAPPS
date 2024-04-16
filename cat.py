try:
    with open(args[1].replace("./","/").replace("/","./"),"r+") as file:
        print(file.read())
except:
    print("[red bold]ERROR:No such file or no file specified !")