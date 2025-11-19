import torch
import torchxrayvision as xrv

# Load model once
model = xrv.models.DenseNet(weights="densenet121-res224-all")
model.eval()

# Preprocess function
def preprocess_image(img):
    # img: PIL.Image in grayscale or RGB
    import torchvision.transforms as transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485], [0.229])  # xrv expects normalized grayscale
    ])
    if img.mode != "L":
        img = img.convert("L")
    return transform(img).unsqueeze(0)  # batch dimension
