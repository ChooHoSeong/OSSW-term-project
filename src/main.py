from variables import *
from functions import main_process

while True:
    option = 0
    try:
        Termianl.reset()
        print(init_page)
        option = int(input("> "))
        print("")
    except:
        print("[!] Please enter a number...")
        Termianl.wait()
        continue

    if option == 1:
        print("[ ] Run the system.")
        main_process()
        print("[ ] Process is done...")
        print("[ ] Program go backs to the first page...\n")
        Termianl.wait()
    elif option == 2:
        Termianl.reset()
        print(how_to_install)
        Termianl.wait()
    elif option == 3:
        Termianl.reset()
        print(contributors)
        Termianl.wait()
    elif option == 4:
        print("[ ] Program is done...\n")
        Termianl.wait()
        exit()
    else:
        print("[!] Not found commend. You should enter one of numbers from 1 to 4")
        os.system("pause")