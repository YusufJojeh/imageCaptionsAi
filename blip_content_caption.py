import os
import json
import requests
import gradio as gr
from PIL import Image
import io
import numpy as np
from transformers import AutoProcessor, BlipForConditionalGeneration
from datetime import datetime

# IBM Watson API Configuration (for reference)
API_KEY = "06rMO9i-askaFv7dpVcRflh1g9j3W5iHz48BYprnCLU8"
SERVICE_URL = "https://api.au-syd.assistant.watson.cloud.ibm.com/instances/9d6735a9-deef-4eb7-8477-2aed315d8245"

# Load the pretrained BLIP processor and model
print("Loading BLIP model...")
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("BLIP model loaded successfully!")

def analyze_image_with_blip(image):
    """Analyze image content using BLIP model"""
    try:
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Process the image with BLIP
        inputs = processor(image, return_tensors="pt")
        
        # Generate caption
        out = model.generate(**inputs, max_length=50, num_beams=5)
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        # Get image properties
        width, height = image.size
        aspect_ratio = width / height
        total_pixels = width * height
        
        # Create analysis data
        analysis_data = {
            'blip_caption': caption,
            'image_properties': {
                'dimensions': f"{width}x{height}",
                'aspect_ratio': round(aspect_ratio, 2),
                'total_pixels': f"{total_pixels:,}",
                'resolution_quality': get_resolution_quality(total_pixels)
            },
            'model_info': {
                'model_name': 'Salesforce/blip-image-captioning-base',
                'model_type': 'BLIP (Bootstrapping Language-Image Pre-training)',
                'capabilities': 'Content-aware image captioning'
            },
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        return caption, analysis_data
        
    except Exception as e:
        error_msg = f"Error analyzing image with BLIP: {str(e)}"
        return error_msg, {"error": error_msg}

def get_resolution_quality(total_pixels):
    """Get resolution quality description"""
    if total_pixels > 12000000:  # 12MP
        return "ultra-high definition"
    elif total_pixels > 5000000:  # 5MP
        return "high definition"
    elif total_pixels > 2000000:  # 2MP
        return "standard definition"
    else:
        return "low resolution"

def create_caption_from_image(image):
    """Main function to create BLIP-based content caption"""
    if image is None:
        return "Please upload an image first.", {"error": "No image provided"}
    
    try:
        caption, analysis_data = analyze_image_with_blip(image)
        
        # Ensure analysis_data is a valid dictionary
        if isinstance(analysis_data, dict):
            return caption, analysis_data
        else:
            return caption, {"error": "Invalid analysis data format"}
            
    except Exception as e:
        error_msg = f"Error processing image: {str(e)}"
        return error_msg, {"error": error_msg}

# Create Gradio interface
def create_interface():
    with gr.Blocks(title="BLIP Image Content Analysis", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🤖 BLIP Image Content Analysis")
        gr.Markdown("Upload an image to get accurate content descriptions using the BLIP AI model")
        
        with gr.Row():
            with gr.Column(scale=1):
                input_image = gr.Image(
                    label="Upload Image",
                    type="pil",
                    height=400
                )
                analyze_btn = gr.Button("🤖 Analyze with BLIP", variant="primary", size="lg")
            
            with gr.Column(scale=1):
                output_caption = gr.Textbox(
                    label="BLIP Content Description",
                    lines=6,
                    placeholder="BLIP-generated content description will appear here..."
                )
                analysis_output = gr.JSON(
                    label="Analysis Details",
                    visible=True
                )
        
        # Add feature descriptions
        gr.Markdown("### 🤖 BLIP Model Features:")
        gr.Markdown("- **Advanced AI**: Uses Salesforce BLIP model for content understanding")
        gr.Markdown("- **Content-Aware**: Accurately describes objects, people, scenes, and actions")
        gr.Markdown("- **Natural Language**: Generates human-like descriptions")
        gr.Markdown("- **High Accuracy**: State-of-the-art image captioning performance")
        gr.Markdown("- **Comprehensive Analysis**: Provides detailed content descriptions")
        gr.Markdown("- **Technical Details**: Includes image properties and model information")
        
        # Event handlers
        analyze_btn.click(
            fn=create_caption_from_image,
            inputs=[input_image],
            outputs=[output_caption, analysis_output]
        )
        
        input_image.change(
            fn=create_caption_from_image,
            inputs=[input_image],
            outputs=[output_caption, analysis_output]
        )
    
    return demo

if __name__ == "__main__":
    print("Starting BLIP Image Content Analysis...")
    print("API Key:", API_KEY[:10] + "...")
    print("Service URL:", SERVICE_URL)
    
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    ) 