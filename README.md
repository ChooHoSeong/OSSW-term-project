# Motion Traking Mouse

<div>
   <video src="motion traking mouse - demo.mp4">
</div>

<br>

__By using this system, you can control a mouse through a hand video sent from a cam.__

&nbsp;The program looks for landmarks in the hands observing with a cam and determines what the user is doing by the distance of certain landmarks. And it performs the function of a mouse in software according to its actions.

<br>

# Requirements

- [mediapipe](https://pypi.org/project/mediapipe): 0.10.8
- [mouse](https://pypi.org/project/mouse/): 0.7.1
- [opencv-python](https://pypi.org/project/opencv-python/): 4.8.1.78
- [screeninfo](https://pypi.org/project/screeninfo/): 0.8.1

### How to install these

First, download the repo to the local computer.  
Then go to the path to repo and enter the following command at the comment prompt.

```ssh
$ pip install -r requirments.txt
```

<br>

# Quick Start

### * Should install requirements before starting and prepare cam

Move to the root path of repo, and run __main.py__