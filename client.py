import cv2


cam = cv2.VideoCapture("rtsp://<your_computer_ip>/live.sdp")

cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cam.set(cv2.CAP_PROP_FPS, 30)

while True:
    ret, frame = cam.read()

    # print(frame.shape)

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()