import cv2
import time
import mouse
import mediapipe as mp
from screeninfo import get_monitors
from variables import *


# Resolution Mapping
def scale(x, input_range, output_range):
    D, A = input_range
    B, C = output_range
    y = (x - A) * (B - C) / (D - A) + C
    return y

# The distance between 2 points
def calculate_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Calculate the area of triangle by using 3 points
def calculate_triangle_area(p0, p5, p17):
    a = calculate_distance(p0, p5)
    b = calculate_distance(p5, p17)
    c = calculate_distance(p17, p0)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Motion Capture Mouse
def main_process():

    print("[ ] Initiating major variables...", end="")
    # get the resolution of your monitor
    myMonitor = get_monitors()[0]
    # init the last position of hand
    last_hand_position = (0, 0)
    # set sensitivity
    # (the larger this value, the more insensitive the mouse movement becomes)
    sensitivity = 4
    # init Mediapipe's [hands] module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)  # detect 1 hand
    # the times of FPS
    prev_frame_time = 0
    new_frame_time = 0
    print(" (done)")

    # init web-cam
    print("[ ] Checking your cam...")
    cap = cv2.VideoCapture(0)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    if cap.isOpened() is False:
        print("\n[!] Could not open your cam...")
        return
    else:
        print(" (done)")

    print("[ ] Start the program")
    print("[ ] If you wanna execute it, enter [q] or [Q]")
    while cap.isOpened():
        ret, frame = cap.read()         # read cam
        new_frame_time = time.time()    # time of new frame
        if not ret:
            continue

        # Frame preprocessing
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5) # resize
        frame = cv2.flip(frame, 1)  # horizontal inversion
        h, w, c = frame.shape   # frame's height, width, and chennals
        cvted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR-> RGB
        
        # detect a hand
        results = hands.process(cvted)

        # If hand is detected
        # Randering landmarks & handle a mouse
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Landmark positions
                highlight_landmarks = [0, 4, 5, 8, 12, 16, 17, 20]
                landmark_positions = {}
                for id, lm in enumerate(hand_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    landmark_positions[id] = (cx, cy)
                    if (id in highlight_landmarks) and (cam_display is True):
                        cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                # Center of a hand (appeared triangle)
                cx = (landmark_positions[0][0] + landmark_positions[5][0] + landmark_positions[17][0]) // 3
                cy = (landmark_positions[0][1] + landmark_positions[5][1] + landmark_positions[17][1]) // 3
                if cam_display is True:
                    # draw center of a hand
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                    # draw triange
                    cv2.line(frame, landmark_positions[0], landmark_positions[5], (255, 0, 0), 2)
                    cv2.line(frame, landmark_positions[5], landmark_positions[17], (255, 0, 0), 2)
                    cv2.line(frame, landmark_positions[17], landmark_positions[0], (255, 0, 0), 2)
                    # Draw a line between index and thumb, middle and thumb
                    cv2.line(frame, landmark_positions[8], landmark_positions[4], (0, 255, 0), 2)
                    cv2.line(frame, landmark_positions[12], landmark_positions[4], (0, 255, 0), 2)

                # calculate triangle's area
                hand_area = calculate_triangle_area(landmark_positions[0], landmark_positions[5], landmark_positions[17])

                # Only when palm area is large enough
                # Move mouse cursor and create click events 
                if hand_area > 3000:  # area threshold
                    if debug_print is True:
                        print(cx,cy,myMonitor.width,myMonitor.height)
                    cx = scale(cx, (100,850),(0,myMonitor.width))
                    cy = scale(cy, (100,450),(0,myMonitor.height))

                    # If the position of a hand is changed, mouse is moved
                    if abs(cx - last_hand_position[0]) > sensitivity or abs(cy - last_hand_position[1]) > sensitivity:
                        mouse.move(cx, cy, absolute=True)
                        last_hand_position = (cx, cy)

                    # distance between index and thumb
                    distance_index_thumb = calculate_distance(landmark_positions[8], landmark_positions[4])
                    # distance between index and thumb
                    distance_middle_thumb = calculate_distance(landmark_positions[12], landmark_positions[4])

                    # Determine if click or not through the distance between fingers
                    if distance_index_thumb < 30:
                        mouse.click()
                        if debug_print is True:
                            print("[/] L-clicked")
                    elif distance_middle_thumb < 30:
                        mouse.click(button='right')
                        if debug_print is True:
                            print("[/] R-clicked")

                elif cam_display is True:
                    cv2.putText(frame, "error - shape of hand is strange", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # compute and display FPS
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps_display = f"FPS: {int(fps)}"
        if cam_display is True:
            cv2.putText(frame, fps_display, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        elif debug_print is True:
            print("[/]", fps_display)

        # show frame
        if cam_display is True:
            cv2.imshow('Hand Tracking', frame)

        # for escaping loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # exit process
    print("[ ] Release the cam...", end="")
    cap.release()
    cv2.destroyAllWindows()
    print(" (done)")
