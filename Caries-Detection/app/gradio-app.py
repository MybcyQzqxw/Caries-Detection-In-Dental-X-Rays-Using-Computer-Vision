import gradio as gr
from predict import predict

def gradio_predict(image: gr.Image):
    # Convert Gradio image to PIL Image
    img_pil = image.convert("RGB")
    
    # Get predictions
    img_with_boxes, status = predict(img_pil)
    
    # Convert PIL image to bytes for Gradio
    return img_with_boxes, status

iface = gr.Interface(
    fn=gradio_predict,
    inputs=gr.Image(type="pil"),
    outputs=[gr.Image(type="pil"), gr.Textbox(label="Detection Status")],
    title="Caries Detection in Dental X-Rays",
    description="Upload a dental X-ray image to detect caries. A bounding box will be drawn only if caries are detected, and a status message will indicate whether caries were found."
)

if __name__ == "__main__":
    iface.launch(debug=True)
