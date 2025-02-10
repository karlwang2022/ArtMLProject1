from flask import Flask, render_template, request, send_file, session
from utils import *

app = Flask(__name__)
app.secret_key = session_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    headlines, additional_data = fetch_headlines(query)
    session['additional_data'] = additional_data
    return render_template('index.html', headlines=headlines, additional_data=additional_data)

@app.route('/article', methods=['GET'])
def article():
    article_id = request.args.get('id')
    additional_data = session.get('additional_data')
    article_content = fetch_article_content(article_id, additional_data)
    return render_template('article.html', article=article_content)


if __name__ == '__main__':
    app.run(debug=True)