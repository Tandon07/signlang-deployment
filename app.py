from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    os.system("python yolov5/detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
    # Add any additional code to process the results if needed

    return "Sign language detection completed!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
