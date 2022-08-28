from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/result", methods = ['POST','GET'])
def result():
    output = request.form.to_dict()
    url = output["url"]

    return render_template("index.html", url = url)

if __name__ == "__main__":
    app.run(debug=True)