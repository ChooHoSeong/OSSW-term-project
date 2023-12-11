import os
from test import main

class Termianl:
    def reset():
        os.system('cls' if os.name == 'nt' else 'clear')
    def wait():
        os.system("pause")

init_page = """
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ** Motion Traking Mouse **                                     │
│                                                                 │
│  This system have you control a mouse through a hand video of   │
│  a web cam                                                      │
│                                                                 │
│  Please enter the number of commend you want to run             │
│                                                                 │
│    1. Run main system                                           │
│    2. how to install requirements                               │
│    3. contributors                                              │
│    4. exit                                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
"""

how_to_install = """
[?] Requirements

  - mediapipe
  - mouse
  - opencv-python
  - screeninfo


[?] how to install these

First, download the repo to the local computer.
Then go to the path to repo and enter the following command at the comment prompt.

┌─────────────────────────────────────────────────────────────────┐
│ $ pip install -r requirments.txt                                │
└─────────────────────────────────────────────────────────────────┘


(If pressed any key, you'll return the first page...)
"""

contributors = """
< AIIA OSSW Unit >

The group for team project of 'Open Source SW' class in Gachon University

[ ] organization: Gachon University
[ ] members (Github ID):
  - ChooHoSeong (Leader)
  - kug4586
  - MrPiclu
  - hoo-n2


(If pressed any key, you'll return the first page...)
"""

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
        main()
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
        exit()
    else:
        print("[!] Not found commend. You should enter one of numbers from 1 to 4")
        os.system("pause")