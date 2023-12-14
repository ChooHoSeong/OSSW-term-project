import os

# To handle things displaying in termianl
class Termianl:
    def reset():  # Clean a terminal
        os.system('cls' if os.name == 'nt' else 'clear')
    def wait():   # wait until pressed any key
        os.system("pause")

# For debugging and cam
cam_display = True
debug_print = True

# Main Interface
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
# Way to install packages
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

# To show Who develop this project
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