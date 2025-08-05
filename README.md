# Image Captioning with BLIP AI Model

This project provides accurate image captioning using the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model. The BLIP model is a state-of-the-art vision-language model that can understand and describe image content with high accuracy.

## 🚀 Features

- **Advanced AI**: Uses Salesforce BLIP model for content understanding
- **Content-Aware**: Accurately describes objects, people, scenes, and actions
- **Natural Language**: Generates human-like descriptions
- **High Accuracy**: State-of-the-art image captioning performance
- **Web Interface**: User-friendly Gradio interface
- **Technical Details**: Includes image properties and model information

## 📁 Project Structure

```
imageCaptions/
├── blip_content_caption.py    # Main BLIP application with Gradio interface
├── image_cap.py              # Simple BLIP script for command-line use
├── test_image.jpg            # Sample image for testing
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
└── my_env/                   # Virtual environment
```

## 🛠️ Setup

### 1. Create Virtual Environment
```bash
pip3 install virtualenv
virtualenv my_env
source my_env/bin/activate  # On Windows: my_env\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Test Image (Optional)
```bash
curl -o test_image.jpg https://images.unsplash.com/photo-1519125323398-675f0ddb6308
```

## 🎯 Usage

### Option 1: Web Interface (Recommended)
Run the main BLIP application with a user-friendly web interface:

```bash
python blip_content_caption.py
```

This will:
- Load the BLIP model (may take a few minutes on first run)
- Start a web server at `http://localhost:7860`
- Provide a Gradio interface for uploading and analyzing images

### Option 2: Command Line
Use the simple script for quick testing:

```bash
python image_cap.py
```

This will analyze the `test_image.jpg` file and print the caption to the console.

## 🔧 Configuration

The applications use the following BLIP model:
- **Model**: `Salesforce/blip-image-captioning-base`
- **Type**: BLIP (Bootstrapping Language-Image Pre-training)
- **Capabilities**: Content-aware image captioning

## 📊 Example Output

When you upload an image, the application will provide:

1. **Content Description**: Natural language description of what's in the image
2. **Analysis Details**: Technical information including:
   - Image dimensions and aspect ratio
   - Resolution quality
   - Model information
   - Timestamp

## 🎨 Supported Image Formats

- JPEG/JPG
- PNG
- BMP
- TIFF
- WebP

## ⚠️ Important Notes

- **First Run**: The BLIP model will be downloaded on first use (~1.2GB)
- **Memory**: The model requires approximately 2-3GB of RAM
- **Processing Time**: Analysis typically takes 2-5 seconds per image
- **Internet**: Required for initial model download and Gradio sharing

## 🐛 Troubleshooting

### Common Issues

1. **Out of Memory Error**
   - Close other applications to free up RAM
   - Use smaller images if possible

2. **Model Download Issues**
   - Check internet connection
   - Clear Hugging Face cache: `rm -rf ~/.cache/huggingface`

3. **Import Errors**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

4. **Gradio Issues**
   - Check if port 7860 is available
   - Try different port: modify `server_port` in the code

## 📈 Performance

The BLIP model provides:
- **High Accuracy**: State-of-the-art performance on image captioning tasks
- **Fast Processing**: 2-5 seconds per image
- **Robust Analysis**: Works well with various image types and content

## 🤝 Contributing

This project uses the BLIP model from Salesforce. For more information about BLIP:
- [BLIP Paper](https://arxiv.org/abs/2201.12086)
- [Hugging Face Model](https://huggingface.co/Salesforce/blip-image-captioning-base)

## 📄 License

This project is for educational and research purposes. The BLIP model is subject to Salesforce's license terms. 