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
    return res, headlines

def fetch_article_content(article_id, headlines):
    index = int(article_id) - 1
    if index < 0 or index >= len(headlines):
        return "Invalid article ID"
    article = get_article(headlines[index][0], headlines[index][1])
    portions = split_article(article, 3)
    prompts = [get_image_prompt(portion) for portion in portions]
    images = [get_image(prompt) for prompt in prompts]
    res =  list(zip(portions, images, prompts))
    print(res)
    return res