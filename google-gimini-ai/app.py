from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from PIL import Image
import io
from front import get_html  # Import the get_html function from front.py

# Initialize Flask app
app = Flask(__name__)

# Configure Google Generative AI with your API key
os.environ["GEMINI_API_KEY"] = ""
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Home route that serves the HTML form
@app.route('/')
def home():
    return get_html()

# Route to generate content from user input
@app.route('/generate', methods=['POST'])
def generate_content():
    prompt = request.form.get('prompt')  # Get the text prompt from the form
    image_file = request.files.get('image')  # Get the uploaded image file

    # Initialize the generative model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if image_file:
        # Open the image using PIL
        image = Image.open(io.BytesIO(image_file.read()))
        
        # Generate content with both text and image inputs
        response = model.generate_content([prompt, image])
    else:
        # Generate content with only text input if no image is provided
        response = model.generate_content(prompt)
    
    return jsonify({"response": response.text})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
