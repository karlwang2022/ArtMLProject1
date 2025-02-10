from flask import Flask, render_template, request, send_file
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    headlines = fetch_headlines(query)
    return render_template('index.html', headlines=headlines)


if __name__ == '__main__':
    app.run(debug=True)