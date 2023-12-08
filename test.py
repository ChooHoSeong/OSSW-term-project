import cv2
import mediapipe as mp
import time
import mouse
from screeninfo import get_monitors

# 사용되는 컴의 해상도 가져오기
myMonitor = get_monitors()[0]

#해상도 매핑 합수
def scale(x, input_range, output_range):
    D, A = input_range
    B, C = output_range
    y = (x - A) * (B - C) / (D - A) + C
    return y

# 마지막 손바닥 위치 초기화
last_hand_position = (0, 0)
# 감도 설정 (이 값이 클수록 마우스 움직임이 더 둔감해집니다)
sensitivity = 4

# Mediapipe 손 모듈 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # 한 손만 인식하도록 설정

# 웹캠 초기화
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# FPS 계산을 위한 초기 시간
prev_frame_time = 0
new_frame_time = 0



# 거리 계산 함수
def calculate_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# 삼각형의 넓이 계산 함수
def calculate_triangle_area(p0, p5, p17):
    # 헤론의 공식 사용
    a = calculate_distance(p0, p5)
    b = calculate_distance(p5, p17)
    c = calculate_distance(p17, p0)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # 프레임 크기 조정 및 좌우 반전
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    frame = cv2.flip(frame, 1)

    # 새로운 프레임의 시간
    new_frame_time = time.time()

    # BGR에서 RGB로 변환
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 손 감지
    results = hands.process(frame)

    # 원래 BGR로 다시 변환
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 감지된 손이 있으면 랜드마크 랜더링 및 마우스 커서 제어
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 랜드마크 위치 저장
            highlight_landmarks = [0, 4, 5, 8, 12, 16, 17, 20]
            landmark_positions = {}
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_positions[id] = (cx, cy)
                if id in highlight_landmarks:
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            # 손바닥 중심(삼각형 중점) 계산
            cx = (landmark_positions[0][0] + landmark_positions[5][0] + landmark_positions[17][0]) // 3
            cy = (landmark_positions[0][1] + landmark_positions[5][1] + landmark_positions[17][1]) // 3
            cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            # 삼각형 그리기
            cv2.line(frame, landmark_positions[0], landmark_positions[5], (255, 0, 0), 2)
            cv2.line(frame, landmark_positions[5], landmark_positions[17], (255, 0, 0), 2)
            cv2.line(frame, landmark_positions[17], landmark_positions[0], (255, 0, 0), 2)

            # 인덱스 팁과 엄지 팁, 중지 팁과 엄지 팁 사이 선 그리기
            cv2.line(frame, landmark_positions[8], landmark_positions[4], (0, 255, 0), 2)
            cv2.line(frame, landmark_positions[12], landmark_positions[4], (0, 255, 0), 2)

            # 손바닥 넓이 계산
            hand_area = calculate_triangle_area(landmark_positions[0], landmark_positions[5], landmark_positions[17])

            # 손바닥 넓이가 충분히 클 때만 마우스 커서 이동 및 클릭 이벤트 생성
            if hand_area > 3000:  # 넓이 임계값
                # 화면 해상도에 맞게 손q 위치 조정
                # screen_w, screen_h = mouse.get_position()
                # x = int(screen_w * (cx / w))
                # y = int(screen_h * (cy / h))
                print(cx,cy,myMonitor.width,myMonitor.height)
                cx = scale(cx, (100,850),(0,myMonitor.width))
                cy = scale(cy, (100,450),(0,myMonitor.height))
                # 손바닥의 중심 위치가 충분히 변했는지 확인
                if abs(cx - last_hand_position[0]) > sensitivity or abs(cy - last_hand_position[1]) > sensitivity:
                    mouse.move(cx, cy, absolute=True)
                    last_hand_position = (cx, cy)

                # 인덱스 팁과 엄지 팁 사이 거리
                distance_index_thumb = calculate_distance(landmark_positions[8], landmark_positions[4])

                # 중지 팁과 엄지 팁 사이 거리
                distance_middle_thumb = calculate_distance(landmark_positions[12], landmark_positions[4])

                # 클릭 판단
                if distance_index_thumb < 30:  # 인덱스 팁과 엄지 팁 사이 거리 임계값
                    mouse.click()
                    print("L-clicked")
                elif distance_middle_thumb < 30:  # 중지 팁과 엄지 팁 사이 거리 임계값
                    mouse.click(button='right')
                    print("R-clicked")

            else:
                cv2.putText(frame, "error - shape of hand is strange", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # FPS 계산 및 표시
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps_display = f"FPS: {int(fps)}"
    cv2.putText(frame, fps_display, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 결과 표시
    cv2.imshow('Hand Tracking', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()
