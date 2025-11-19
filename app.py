from flask import Flask, request, render_template, jsonify
from xray_model import model, preprocess_image
from utils import allowed_file, check_file_size, dicom_to_image
from PIL import Image
import time
import torch
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if not file or not allowed_file(file.filename):
            return "Invalid file type"
        if not check_file_size(file):
            return "File too large"

        if file.filename.endswith(".dcm"):
            img = dicom_to_image(file)
        else:
            img = Image.open(file)

        start = time.time()
        input_tensor = preprocess_image(img)
        preprocess_time = time.time() - start

        start = time.time()
        with torch.no_grad():
            outputs = model(input_tensor)
        inference_time = time.time() - start

        probs = torch.sigmoid(outputs).numpy()[0]
        labels = model.pathologies

        results = list(zip(labels, probs))
        return render_template("results.html", results=results,
                               preprocess_time=preprocess_time,
                               inference_time=inference_time)
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def api_predict():
    file = request.files["file"]
    # Repeat same logic as above
    # Return JSON with probabilities + latency
    return jsonify({"msg": "Implement JSON API here"})

if __name__ == "__main__":
    app.run(debug=True)
