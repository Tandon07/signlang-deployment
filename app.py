# from flask import Flask, render_template, request
# import os
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/detect', methods=['POST'])
# def detect():
#     os.system("python yolov5/detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
#     # Add any additional code to process the results if needed
#
#     return "Sign language detection completed!"
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)




from flask import Flask, render_template, request
import os
import signal
import subprocess

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    os.system("python yolov5/detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
    # Add any additional code to process the results if needed

    return "Sign language detection completed!"
camera_process = None
@app.route('/control', methods=['POST'])
def control():
    global camera_process
    action = request.form.get('action')
    if action == 'start':
        if camera_process is None:
            camera_process = subprocess.Popen("python yolov5/detect.py --weights best.pt --img 416 --conf 0.5 --source 0", shell=True)
    elif action == 'stop':
        if camera_process is not None:
            camera_process.terminate()
            camera_process = None
        else:
            os.kill(os.getpid(), signal.SIGTERM)

    return "Action performed: " + action

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
