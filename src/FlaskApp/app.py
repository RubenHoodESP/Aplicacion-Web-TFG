import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'datos'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/borrar")
def borrar():
    imagenes = os.listdir('static/imagenes')
    for file in imagenes:
        os.remove('static/imagenes/' + file)
    return render_template('borrado.html')


@app.route("/subido", methods = ['POST', 'GET'])
def subir():
    if request.method == 'POST':
        f = request.files['file[]']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        os.system('python3 Main.py')
    return render_template('subido.html')

@app.route("/subido/imagen", methods = ['POST', 'GET'])
def imagen():
    imagenes = os.listdir('static/imagenes')
    imagenes = ['imagenes/' + file for file in imagenes]
    return render_template('imagen.html', imagenes = imagenes)


if __name__ == "__main__":
    app.run(host='localhost', port=5050)
