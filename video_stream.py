import cv2

cam = cv2.VideoCapture(0, apiPreference=cv2.CAP_ANY, params=[
    cv2.CAP_PROP_FRAME_WIDTH, 1920,
    cv2.CAP_PROP_FRAME_HEIGHT, 1080,
    cv2.CAP_PROP_FPS, 30])

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()