from flask import Flask, Response
import cv2

app = Flask(__name__)

def generate_video():
    cap = cv2.VideoCapture(0, apiPreference=cv2.CAP_ANY, params=[
        cv2.CAP_PROP_FRAME_WIDTH, 1920,
        cv2.CAP_PROP_FRAME_HEIGHT, 1080,
        cv2.CAP_PROP_FPS, 30])
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Encode frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        # Convert JPEG to bytes and yield as a response
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)