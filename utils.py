import os, pydicom
from PIL import Image
import io

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "dcm"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_file_size(file):
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    return size <= MAX_FILE_SIZE

def dicom_to_image(dicom_file):
    ds = pydicom.dcmread(dicom_file)
    ds.PatientName = "Anonymous"  # de-identify
    arr = ds.pixel_array
    img = Image.fromarray(arr).convert("L")
    return img
