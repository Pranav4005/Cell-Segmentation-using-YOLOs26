from ultralytics import YOLO

# Load trained model
model = YOLO(
    "artifacts/model_trainer/best.pt"
)

# Run prediction on test images
results = model.predict(
    source="artifacts/data_ingestion/feature_store/dataset/test/images",
    save=True,
    conf=0.25
)

print("Prediction completed")