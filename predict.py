from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import numpy as np
import tflite
from PIL import Image
from numpy import asarray
import tflite_runtime.interpreter as tflite
tflite_runtime.interpreter.Interpreter

app = Flask(__name__)

# Load the model



class_names = ['Alternaria', 'Anthracnose', 'Black Mould Rot', 'Healthy', 'Stem and Rot']
BATCH_SIZE = 32
IMAGE_SIZE = 255
CHANNEL = 3
EPOCHS = 30

# Function to check if the file has an allowed extension
'''def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}'''

# Function to preprocess and predict
def predict(img):
    img_array = asarray(img)
    img_array = np.expand_dims(img_array, 0)

    interpreter = tflite.Interpreter(model_path='converted_model.tflite')
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']

    interpreter.set_tensor(input_index, img_array)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    predicted_class = class_names[np.argmax(preds[0])]
    confidence = round(100 * (np.max(preds[0])), 2)
    return predicted_class, confidence

# Route to the home page

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']  # Corrected line

        # If the user does not select a file, browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', message='No selected file')

        # If the file is allowed and has an allowed extension
        if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}:
            filename = secure_filename(file.filename)
            filepath = os.path.join('.venv/static', filename)
            file.save(filepath)

            # Read the image
            img = Image.open(filepath)
            img = img.resize((255, 255))
            # Predict using the loaded model
            predicted_class, confidence = predict(img)

            # Render the template with the uploaded image, actual and predicted labels, and confidence
            return render_template('index.html', image_path=filepath, actual_label=predicted_class, predicted_label=predicted_class, confidence=confidence)

    return render_template('index.html', message='Upload an image')

if __name__ == '__main__':
    app.run(debug=True)