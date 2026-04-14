import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)

cap = cv2.VideoCapture(0)

canvas = None

# Smoothing
prev_x, prev_y = 0, 0
smoothening = 7

# Brush settings
draw_color = (255, 0, 255)
brush_thickness = 8
eraser_thickness = 40

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    if canvas is None:
        canvas = np.zeros_like(img)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        # Index finger
        x1 = int(hand.landmark[8].x * w)
        y1 = int(hand.landmark[8].y * h)

        # Middle finger
        x2 = int(hand.landmark[12].x * w)
        y2 = int(hand.landmark[12].y * h)

        # Smooth coordinates
        curr_x = prev_x + (x1 - prev_x) // smoothening
        curr_y = prev_y + (y1 - prev_y) // smoothening

        # Distance between fingers
        distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

        # DRAW MODE (fingers close)
        if distance < 40:
            cv2.circle(img, (curr_x, curr_y), 6, draw_color, -1)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = curr_x, curr_y

            cv2.line(canvas, (prev_x, prev_y), (curr_x, curr_y),
                     draw_color, brush_thickness)

            prev_x, prev_y = curr_x, curr_y

            cv2.putText(img, "DRAW", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        # MOVE MODE
        elif distance > 60:
            prev_x, prev_y = 0, 0
            cv2.putText(img, "MOVE", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        # ERASE MODE (medium distance)
        else:
            cv2.circle(img, (curr_x, curr_y), 20, (0, 0, 0), -1)

            cv2.line(canvas, (prev_x, prev_y), (curr_x, curr_y),
                     (0, 0, 0), eraser_thickness)

            prev_x, prev_y = curr_x, curr_y

            cv2.putText(img, "ERASE", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    else:
        prev_x, prev_y = 0, 0

    # Merge canvas
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)

    cv2.imshow("PRO Drawing System", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
