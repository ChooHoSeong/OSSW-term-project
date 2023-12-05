import cv2
import mediapipe as mp
import time


def get_finger_landmarks(hand_landmarks, finger_indices):
    result = [hand_landmarks.landmark[index] for index in finger_indices]
    # print(result)
    return result

def calculate_distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


# MediaPipe 손 모듈 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# 웹캠 시작
cap = cv2.VideoCapture(0)

# 이전 프레임 시간
prev_frame_time = 0

# 지금 프레임 시간
new_frame_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # 현재 시간 업데이트
    new_frame_time = time.time()

    # 처리속도 향상을 위한 리사이즈
    frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)


    # BGR 이미지를 RGB로 변환
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # MediaPipe로 손 인식
    results = hands.process(frame_rgb)

    
    if results.multi_hand_landmarks:
        # 손 랜드마크 그리기
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # 손가락 랜드마크 인덱스
            THUMB_LANDMARKS = [mp_hands.HandLandmark.THUMB_TIP,
                               mp_hands.HandLandmark.THUMB_IP,
                               mp_hands.HandLandmark.THUMB_MCP,
                               mp_hands.HandLandmark.THUMB_CMC]
            INDEX_FINGER_LANDMARKS = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                                      mp_hands.HandLandmark.INDEX_FINGER_DIP,
                                      mp_hands.HandLandmark.INDEX_FINGER_PIP,
                                      mp_hands.HandLandmark.INDEX_FINGER_MCP]
            MIDDLE_FINGER_LANDMARKS = [mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                                       mp_hands.HandLandmark.MIDDLE_FINGER_DIP,
                                       mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
                                       mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            RING_FINGER_LANDMARKS = [mp_hands.HandLandmark.RING_FINGER_TIP,
                                     mp_hands.HandLandmark.RING_FINGER_DIP,
                                     mp_hands.HandLandmark.RING_FINGER_PIP,
                                     mp_hands.HandLandmark.RING_FINGER_MCP]
            PINKY_FINGER_LANDMARKS = [mp_hands.HandLandmark.PINKY_TIP,
                                      mp_hands.HandLandmark.PINKY_DIP,
                                      mp_hands.HandLandmark.PINKY_PIP,
                                      mp_hands.HandLandmark.PINKY_MCP]

            # 엄지손가락 랜드마크
            thumb_landmarks = get_finger_landmarks(hand_landmarks, THUMB_LANDMARKS)
            # 검지손가락 랜드마크
            index_finger_landmarks = get_finger_landmarks(hand_landmarks, INDEX_FINGER_LANDMARKS)
            # 중지손가락 랜드마크
            middle_finger_landmarks = get_finger_landmarks(hand_landmarks, MIDDLE_FINGER_LANDMARKS)
            # 약지손가락 랜드마크
            ring_finger_landmarks = get_finger_landmarks(hand_landmarks, RING_FINGER_LANDMARKS)
            # 새끼손가락 랜드마크
            pinky_finger_landmarks = get_finger_landmarks(hand_landmarks, PINKY_FINGER_LANDMARKS)


            distance = calculate_distance(thumb_landmarks[0], index_finger_landmarks[0]);
            if distance < 0.1:
                print("clicked")
            else:
                print("none")


    # FPS 계산
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    # FPS 표시
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 3, cv2.LINE_AA)

    # 결과 표시
    cv2.imshow('Hands', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
