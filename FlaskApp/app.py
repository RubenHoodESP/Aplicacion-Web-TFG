import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '../'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/upload", methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return "File saved successfully"

@app.route("/imagen_1", methods = ['POST', 'GET'])
def imagen_1():
    return render_template('imagen_1.html')

@app.route("/imagen_2")
def imagen_2():
    return render_template('imagen_2.html')

@app.route("/imagen_3")
def imagen_3():
    return render_template('imagen_3.html')

@app.route("/imagen_4")
def imagen_4():
    return render_template('imagen_4.html')

@app.route("/imagen_5")
def imagen_5():
    return render_template('imagen_5.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000)