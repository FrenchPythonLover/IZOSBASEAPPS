import sys
from ast import literal_eval
sys.path.append("../lib/")
import base
if base.version < 5.2:
    print("[red bold]ERROR:IZOS version is not equal or superior to 5.2. Aborting...")
    exit()
print("""
IZOS CALCULATOR
[blue]Supported operations: + * - /[/blue]
[green]Ans is supported: Ans is the last Answer [/green]
Type help to exit
""")
ans = 0
running = True
while running:
    
    inp = input(">").replace("Ans",str(ans)).replace("^","**")
    if inp == "exit":
        print("Thanks for using the calculator")
        running = False
    else:
        try:
            ans = eval(inp) # This is totally safe bc the user runs it on his computer (i think)
            print(ans)
        except Exception as ex:
            print("[red bold]ERROR:",ex)
