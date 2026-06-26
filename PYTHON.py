from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
API_TOKEN = "YOUR_HUGGINGFACE_API_TOKEN"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )
    return response.content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']

    image_bytes = generate_image(prompt)

    return send_file(
        BytesIO(image_bytes),
        mimetype='image/png'
    )

if __name__ == '__main__':
    app.run(debug=True)