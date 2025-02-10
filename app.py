from flask import Flask, render_template, request, send_file
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Generate dynamic content based on the query
    image = generate_image(query)
    return send_file(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)