import os
import sys
import shutil

from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    Response
)

from flask_cors import CORS

from ultralytics import YOLO

from src.cellSegmentation.pipeline.training_pipeline import (
    TrainPipeline
)

from src.cellSegmentation.utils.main_utils import (
    decodeImage,
    encodeImageIntoBase64
)

from src.cellSegmentation.constants.application import (
    APP_HOST,
    APP_PORT
)


app = Flask(__name__)

CORS(app)


# Create folders
os.makedirs("data", exist_ok=True)
os.makedirs("runs", exist_ok=True)


# Load trained model once
model = YOLO(
    "artifacts/model_trainer/best.pt"
)


class ClientApp:

    def __init__(self):

        self.filename = "inputImage.jpg"


clApp = ClientApp()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/train")
def trainRoute():

    try:

        obj = TrainPipeline()

        obj.run_pipeline()

        return "Training Successful!!"

    except Exception as e:

        return Response(str(e))


@app.route("/predict", methods=["POST"])
def predictRoute():

    try:

        data = request.get_json()

        image = data["image"]

        # Decode image
        decodeImage(image, clApp.filename)

        input_image_path = os.path.join(
            "data",
            clApp.filename
        )

        # Run prediction
        results = model.predict(
            source=input_image_path,
            conf=0.25,
            save=True
        )

        # Get latest prediction folder
        predict_dirs = sorted(
            [
                d for d in os.listdir(
                    "runs/segment"
                )
                if "predict" in d
            ]
        )

        latest_predict_dir = os.path.join(
            "runs/segment",
            predict_dirs[-1]
        )

        prediction_image_path = os.path.join(
            latest_predict_dir,
            clApp.filename
        )

        # Encode prediction image
        opencodedbase64 = encodeImageIntoBase64(
            prediction_image_path
        )

        result = {
            "image": opencodedbase64.decode("utf-8")
        }

        return jsonify(result)

    except ValueError as val:

        print(val)

        return Response(
            "Value not found inside JSON data"
        )

    except KeyError:

        return Response(
            "Incorrect key passed in JSON"
        )

    except Exception as e:

        print(e)

        return Response(
            f"Error occurred: {str(e)}"
        )

@app.route("/realtime")
def realtimeRoute():

    try:

        os.system("python real_time.py")

        return "Real-time coral segmentation started"

    except Exception as e:

        return Response(
            f"Error occurred: {str(e)}"
        )
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )