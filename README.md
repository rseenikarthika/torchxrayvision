# TorchXRayVision Flask UI Service

## Project Overview
This project implements a **minimal clinical-style web app** around [mlmed/torchxrayvision](https://github.com/mlmed/torchxrayvision). It allows users to upload **chest X-ray images** (JPG, PNG, DICOM) to obtain:

- Predicted pathologies from a **pretrained model**.
- Visual explanation maps (Grad-CAM/Integrated Gradients).

Both a **browser-based UI** and a **JSON REST API** are provided.

---

## Features

### Model
- Loads a **pretrained TorchXRayVision model** (e.g., `densenet121-res224-all`) at app startup.
- Reuses the model instance for multiple requests.

### Input Validation
- Accepts **JPG, PNG, and DICOM** formats.
- **De-identifies DICOM** images before processing.
- **Maximum file size:** 10 MB.
- Rejects unsupported types or oversized files with a clear error message.

### Preprocessing
- Converts images to grayscale if required.
- Normalizes according to model expectations.
- Resizes to model input dimensions.

### Prediction
- Returns **class probabilities** for known pathologies.
- Includes **latency metrics**: preprocessing time and inference time.

### Explainability
- Provides **Grad-CAM heatmap overlay** (or Captum integrated gradients) for at least one predicted class.
- Visualizes heatmap side-by-side with the original image.

### User Interface (UI)
- Simple **upload form**.
- Table of **predicted probabilities**.
- Side-by-side display of **original image and heatmap**.

### REST API
- Programmatic access via **JSON POST request**.
- Returns predictions, heatmaps (base64), and latency metrics.

---

## Project Structure

```
TorchXRayVision/
│
├─ app.py            # Flask app entry point
├─ xray_model.py     # Model loading, preprocessing, inference, explainability
├─ utils.py          # Helper functions (DICOM handling, validation, visualization)
├─ templates/        # HTML templates for UI
├─ static/           # Static assets (CSS, JS, heatmaps)
├─ requirements.txt  # Python dependencies
├─ env/              # Virtual environment (optional)
└─ TorchXRayVision.zip # Optional packaged archive
```

---

## How to Run

1. **Clone the repository**
```bash
git clone https://github.com/rseenikarthika/torchxrayvision.git
cd TorchXRayVision
```

2. **Create environment & install dependencies**
```bash
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate       # Windows
pip install -r requirements.txt
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Access the UI**
Open `http://127.0.0.1:5000` in your browser.

5. **Use REST API**
POST image to `/api/predict` endpoint:
```bash
curl -X POST -F "file=@chest_xray.png" http://127.0.0.1:5000/api/predict
```

---

## Requirements
- Python 3.9+
- Flask
- torch
- torchvision
- torchxrayvision
- numpy
- matplotlib
- pydicom
- opencv-python
- PIL / Pillow
- Captum (optional, for explainability)

---

## Outputs
- Predicted **pathology probabilities**.
- **Grad-CAM heatmaps**.
- **Latency metrics**.
- Browser-based visualization with side-by-side images.

---

## License
This project is open source under the MIT License.
