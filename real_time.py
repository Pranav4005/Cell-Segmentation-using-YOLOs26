from ultralytics import YOLO
import cv2

# Load model
model = YOLO(
    "artifacts/model_trainer/best.pt"
)

# Open webcam
cap = cv2.VideoCapture(
    0,
    cv2.CAP_DSHOW
)

if not cap.isOpened():

    print("Cannot open webcam")

    exit()

try:

    while True:

        ret, frame = cap.read()

        if not ret:

            print("Failed to grab frame")

            break

        # Prediction
        results = model.predict(
            source=frame,
            conf=0.5,
            imgsz=320,
            verbose=False
        )

        annotated_frame = results[0].plot()

        cv2.imshow(
            "Real-Time Coral Segmentation",
            annotated_frame
        )

        # Quit button
        if cv2.waitKey(1) & 0xFF == ord('q'):

            print("Closing webcam...")

            break

finally:

    # ALWAYS release webcam
    cap.release()

    cv2.destroyAllWindows()

    print("Webcam released successfully")