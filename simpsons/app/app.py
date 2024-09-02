import streamlit as st
import torch
from torch import models, transforms
import torch.nn as nn
from PIL import Image

st.title('Simpsons Classification')

# Device configuration (CPU or GPU)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the pre-trained ResNet-50 model structure
resnet = models.resnet50(weights=ResNet50_Weights.DEFAULT)

# Replace the fully connected layer with the one used during fine-tuning
in_features = 2048
out_features = 42  # Number of classes in your dataset
resnet.fc = nn.Linear(in_features, out_features)

# Load the fine-tuned weights
resnet.load_state_dict(torch.load("fine_tuned_resnet50.pth", map_location=DEVICE))
resnet = resnet.to(DEVICE)
resnet.eval()  # Set model to evaluation mode

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image
    image_tensor = preprocess(image).unsqueeze(0)
    
    # Predict the class
    with torch.no_grad():
        output = resnet(image_tensor)
    
    # Get the predicted class
    _, predicted_class = torch.max(output, 1)
    
    st.write(f"Predicted class: {predicted_class.item()}")