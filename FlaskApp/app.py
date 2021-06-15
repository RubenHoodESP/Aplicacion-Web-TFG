from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/imagen_1")
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
    app.run()