from functions import *

def generate_image(query):
    # Example function to generate an image based on the query
    img = Image.new('RGB', (200, 100), color = (73, 109, 137))
    img.save('generated_image.png')
    return io.BytesIO(open('generated_image.png', 'rb').read())