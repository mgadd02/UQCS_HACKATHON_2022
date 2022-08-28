from flask import Flask, render_template, request
from reverse_search import *
from tren import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/result", methods = ['POST','GET'])
def result():
    output = request.form.to_dict()
    url = output["url"]
    tags = quickTags(url)
    trend = check_trends(tags)
    broad = broadTags(url)
    url_list = imageFinder(url, 4)
    sentimentStr = sentiment(url)

    return render_template("index.html", url = url, tags = tags,
     trend = trend, broad = broad, url_list = url_list, sentimentStr = sentimentStr)

if __name__ == "__main__":
    app.run(debug=False)