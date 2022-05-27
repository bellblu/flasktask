from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def name():
    return render_template('index.html')


@app.route('/hello',  methods=["POST", "GET"])
def hello():
    name = request.form['text']
    return render_template('hello.html', name=name)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')