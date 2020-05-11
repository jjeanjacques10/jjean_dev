# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Gravando um vídeo com a Webcam ---
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while True:
    (ret, frame) = cap.read()
    frame = cv2.flip(frame, 1)
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Exit...')
        break

cap.release()
out.release()
cv2.destroyAllWindows()