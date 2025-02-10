from functions import *
import requests

def generate_image(query):
    # Example function to generate an image based on the query
    img = Image.new('RGB', (200, 100), color = (73, 109, 137))
    img.save('generated_image.png')
    return io.BytesIO(open('generated_image.png', 'rb').read())

def tuple_to_string(data_tuple):
    result_string = ""
    for item in data_tuple:
        if isinstance(item, str):
            result_string += item + ". "
        elif isinstance(item, list):
            result_string += '[' + ', '.join(item) + ']. '
        else:
            result_string += str(item) + ". "
    return result_string

def fetch_headlines(query):
    headlines = get_headlines(query, 5)
    res = []
    for i in range(len(headlines)):
        id = i + 1
        title = tuple_to_string(headlines[i])
        dict = {'id': id, 'title': title}
        res.append(dict)
    return res

def fetch_article_content(article_id):
    articles = {
        1: 'Full content of article 1',
        2: 'Full content of article 2',
        3: 'Full content of article 3',
        4: 'Full content of article 4',
        5: 'Full content of article 5'
    }
    return articles.get(int(article_id), 'Article not found')