from ultralytics import YOLO
import os

# Load YOLOv8 model with custom weights
def load_model():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the model file
    model_path = os.path.join(current_dir, '..', 'data', 'best.pt')
    
    # Check if running in Docker container
    if os.path.exists('/app/data/best.pt'):
        return YOLO('/app/data/best.pt')  # Use the path inside the container
    else:
        return YOLO(model_path)  # Use local path
