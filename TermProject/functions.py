"""
인식한 손동작에 따라 마우스가 작동하는 기능을 구현했습니다.

사용한 라이브러리:
- mouse (https://github.com/boppreh/mouse)
"""

import mouse, time

print("if you end this program, please click anything")
while mouse.is_pressed() == False:
    print(f"mouse position: {mouse.get_position()}")
    time.sleep(0.5)