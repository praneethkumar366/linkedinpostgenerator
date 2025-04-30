import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from flask import Flask, request, render_template
import os
from transformers import pipeline, set_seed
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load GPT2/DistilGPT2 model for text generation
generator = pipeline('text-generation', model='distilgpt2')
set_seed(42)

def generate_post(prompt):
    result = generator(
        prompt + "\nI'm happy to share that",
        max_length=120,
        num_return_sequences=1,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    text = result[0]['generated_text']
    hashtags = "\n\n#Achievement #Career #Learning #Success #LinkedInPost"
    return text.strip() + hashtags

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_url = None

    if request.method == 'POST':
        achievement_text = request.form.get('achievement', '')
        file = request.files.get('file')

        # Save uploaded file if present
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_url = file_path.replace("\\", "/")

        # Fallback if no text entered but image is uploaded
        if not achievement_text and file:
            achievement_text = "I earned a new certification!"

        if achievement_text:
            result = generate_post(achievement_text)

    return render_template('index.html', result=result, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
